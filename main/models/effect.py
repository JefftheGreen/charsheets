from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import datetime
from main.default_data import BONUS_TYPE_CHOICES, ABILITY_CHOICES, SAVE_CHOICES
import warnings
from . import Skill


class Effect(models.Model):

    # The type of the owner of this effect. Always User, Sheet, or null.
    # Which one determines some behavior and whether it's displayed on a sheet.
    owner_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                   null=True)
    # The id of the owner. Refers to a user or sheet if not none.
    owner_id = models.PositiveIntegerField(null=True)
    # The owner of the effect. Can be a User, a Sheet
    owner = GenericForeignKey('owner_type', 'owner_id')
    # The time the effect was created
    date = models.DateTimeField(default=datetime.now)
    # Whether the effect is active. If not, it's not factored into the
    # character sheet.
    active = models.BooleanField(default=True)
    # The effect's name. This is displayed on the sheet.
    name = models.CharField(max_length=200)
    # The effect's description. This is displayed on the sheet.
    description = models.CharField(max_length=1000)
    # Sheets can be nested. The ulimate parent (i.e. the effect with no
    # parents) is the one evaluated by a sheet, collecting the results of all
    # sub effects
    parent_effect = models.ForeignKey('self', related_name='sub_effect', 
                                      related_query_name='sub_effect', 
                                      null=True)
    # The bonus amount, if a flat bonus
    bonus_amount = models.IntegerField(default=None, null=True)
    # If the bonus is equal to an ability modifier, this stores the ability
    # using the values in ABILITY_CHOICES.
    x_to_y_bonus_ability = models.IntegerField(default=None,
                                               choices=ABILITY_CHOICES,
                                               null=True)
    # If the effect replaces an ability score in a calculation instead of
    # giving a bonus, this stores the ability using the values in
    # ABILITY_CHOICES.
    x_to_y_replace_ability = models.IntegerField(default=None,
                                                 choices=ABILITY_CHOICES,
                                                 null=True)
    # The bonus type, using the values in BONUS_TYPE_CHOICES
    bonus_type = models.IntegerField(default=18, choices=BONUS_TYPE_CHOICES)
    # If the bonus goes to a skill, this stores the skill
    skill_bonus = models.ForeignKey('Skill', on_delete=models.SET_NULL, 
                                    default=None, null=True)
    # If the bonus goes to an ability, this stores the ability using the values
    # in ABILITY_CHOICES
    ability_bonus = models.IntegerField(choices=ABILITY_CHOICES, default=None, 
                                        null=True)
    # If the bonus goes to a save, this stores the save using the values
    # in SAVE_CHOICES
    save_bonus = models.IntegerField(choices=SAVE_CHOICES, default=None, 
                                     null=True)
    # If the effect overrides a default ability to some statistic, this stores
    # the ability using the values in ABILITY_CHOICES
    override_ability = models.IntegerField(choices=ABILITY_CHOICES,
                                           default=None, null=True)
    # If the effect overrides a save's default ability, this stores the save
    # using the values in SAVE_CHOICES
    save_override = models.IntegerField(choices=SAVE_CHOICES, default=None,
                                        null=True)

    def total_ability_bonus(self, ability):
        bonus = []
        if self.ability_bonus == ability:
            # A fixed bonus
            if self.bonus_amount is not None:
                bonus.append((self.bonus_type, self.bonus_amount))
            # X to Y on abilities really screws things up
            elif self.x_to_y_bonus_ability is not None:
                e = "Effect {0} has from_x_stat for an ability.".format(self.id)
                raise RuntimeError(e)
            # This shouldn't happen
            else:
                w = ("Effect {0} has an ability listed but no bonus amount"
                     .format(self.id))
                warnings.warn(w, RuntimeWarning)
        # Add sub-effect bonuses
        for sub_effect in self.sub_effect.all():
            bonus += sub_effect.total_ability_bonus(ability)
        return bonus

    def total_skill_bonus(self, skill):
        if type(skill) == int:
            skill = Skill.objects.get(id=skill)
        bonus = []
        # Only add if this effect has a bonus to the specified skill
        if self.skill_bonus == skill:
            # A fixed bonus
            if self.bonus_amount is not None:
                bonus.append((self.bonus_type, self.bonus_amount))
            # A bonus equal to an ability score modifier
            elif self.x_to_y_bonus_ability is not None:
                bonus.append((self.bonus_type, self.get_from_x_stat_display()))
            # This shouldn't happen
            else:
                w = "Effect {0} has a skill listed but no bonus amount".format(
                        self.id)
                warnings.warn(w, RuntimeWarning)
        # Add sub-effect bonuses
        for sub_effect in self.sub_effect.all():
            bonus += sub_effect.total_skill_bonus(skill)
        return bonus

    def total_save_bonus(self, save):
        if type(save) == int:
            save = Skill.objects.get(id=save)
        bonus = []
        # Only add if this effect has a bonus to the specified skill
        if self.save_bonus == save:
            # A fixed bonus
            if self.bonus_amount is not None:
                bonus.append((self.bonus_type, self.bonus_amount))
            # A bonus equal to an ability score modifier
            elif self.x_to_y_bonus_ability is not None:
                bonus.append((self.bonus_type, self.get_from_x_stat_display()))
            # This shouldn't happen
            else:
                w = "Effect {0} has a save listed but no bonus amount".format(
                    self.id)
                warnings.warn(w, RuntimeWarning)
        # Add sub-effect bonuses
        for sub_effect in self.sub_effect.all():
            bonus += sub_effect.total_save_bonus(save)
        return bonus


    # Gets the save whose ability the effect overrides.
    #   save:
    #       the save to get bonuses for. integer (see SAVE_CHOICES).
    # Returns a 2-tuple (ability, date added), where ability is an integer
    # from ABILITY_CHOICES and date is a the date the effect or sub-effect
    # was created.
    def ultimate_save_override(self, save):
        overrides = []
        # Getting tuples of (ability, date added)
        if self.save_override == save:
            overrides.append((save, self.date))
        # Do the same for the sub-effects
        for sub_effect in self.sub_effect.all():
            sub_override = sub_effect.save_override
            if sub_override[0] == save:
                overrides.append(sub_override)
        # Sort by date added
        overrides.sort(key=lambda override: override[1])
        # Return the most recent oone
        return overrides[-1]



    @property
    def skill_bonuses(self):
        # Make skill bonus dictionary
        if self.skill_bonus_id is not None:
            # Add own skill bonus if exists
            # Format = {skill: {bonus_type:[bonus1, bonus2, bonus3]
            bonuses = {self.skill_bonus_id:
                            {self.bonus_type:[self.bonus_amount 
                                            if self.bonus_amount is not None
                                            else self.get_from_x_stat_display()]
                                
                            }
                       }
        else:
            bonuses = dict()
        # Add bonuses from sub-effects to bonuses
        for effect in self.sub_effect.all():
            sub_effect_bonuses = effect.skill_bonuses
            for skill in sub_effect_bonuses:
                for bonus_type in sub_effect_bonuses[skill]:
                    if skill in bonuses:
                        if bonus_type in bonuses[skill]:
                            bonuses[skill][bonus_type] += (sub_effect_bonuses
                                                           [skill][bonus_type])
                        else:
                            bonuses[skill][bonus_type] = (sub_effect_bonuses
                                                          [skill][bonus_type])
                    else:
                        bonuses[skill] = {bonus_type: sub_effect_bonuses
                                                      [skill][bonus_type]}
        return bonuses

    def __str__(self):
        return self.name
