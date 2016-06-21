from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from main.default_data import DEFAULT_SAVE_ABILITIES, DEFAULT_CONDITION_EFFECTS
from django.core.exceptions import FieldDoesNotExist, ObjectDoesNotExist
from main.models.effect import Condition
from django.utils.functional import cached_property
import re


class Sheet(models.Model):

    # TODO: Figure out which fields to index
    # The user that created the sheet
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # The time the effect was created
    date = models.DateTimeField(default=timezone.now)
    # The name of the sheet, displayed where the sheet is referred to
    name = models.CharField(max_length=200, blank=True, default='')
    # The character name, displayed on the sheet
    char_name = models.CharField(max_length=200, blank=True, default='')
    # The character race, displayed on the sheet
    race = models.CharField(max_length=200, blank=True, default='')
    # The character classes, displayed on the sheet
    classes = models.CharField(blank=True, max_length=200)
    # The character's gender, displayed on the sheet
    gender = models.CharField(max_length=200, blank=True, default='')
    # The character's alignment, displayed on the sheet
    alignment = models.CharField(max_length=200, blank=True, default='')
    # The character's deity, displayed on the sheet
    deity = models.CharField(max_length=200, blank=True, default='')
    # The campaign the character is for, displayed on the sheet
    campaign = models.CharField(max_length=200, blank=True, default='')
    # The character's age, displayed on the sheet
    age = models.CharField(max_length=200, blank=True, default='')
    # The character's size, displayed on the sheet, and parsed for calculations
    disp_size = models.CharField(max_length=200, blank=True, default='')
    # The character's Str, displayed on the sheet, and parsed for calculations
    disp_base_str = models.CharField(max_length=5, blank=True, default='')
    # The character's Dex, displayed on the sheet, and parsed for calculations
    disp_base_dex = models.CharField(max_length=5, blank=True, default='')
    # The character's Con, displayed on the sheet, and parsed for calculations
    disp_base_con = models.CharField(max_length=5, blank=True, default='')
    # The character's Int, displayed on the sheet, and parsed for calculations
    disp_base_int = models.CharField(max_length=5, blank=True, default='')
    # The character's Wis, displayed on the sheet, and parsed for calculations
    disp_base_wis = models.CharField(max_length=5, blank=True, default='')
    # The character's Cha, displayed on the sheet, and parsed for calculations
    disp_base_cha = models.CharField(max_length=5, blank=True, default='')
    # The character's Will, displayed on the sheet, and parsed for calculations
    disp_base_will = models.CharField(max_length=5, blank=True, default='0')
    # The character's Ref, displayed on the sheet, and parsed for calculations
    disp_base_ref = models.CharField(max_length=5, blank=True, default='0')
    # The character's Fort, displayed on the sheet, and parsed for calculations
    disp_base_fort = models.CharField(max_length=5, blank=True, default='0')
    # Whether the character is blinded
    blinded = models.BooleanField(default=False)
    # Whether the character is confused
    confused = models.BooleanField(default=False)
    # Whether the character is dazed
    dazed = models.BooleanField(default=False)
    # Whether the character is dazzled
    dazzled = models.BooleanField(default=False)
    # Whether the character is deafened
    deafened = models.BooleanField(default=False)
    # Whether the character is disabled
    disabled = models.BooleanField(default=False)
    # Whether the character is dying
    dying = models.BooleanField(default=False)
    # Whether the character is entangled
    entangled = models.BooleanField(default=False)
    # Whether the character is fascinated
    fascinated = models.BooleanField(default=False)
    # Whether the character is flat-footed
    flat_footed = models.BooleanField(default=False)
    # Whether the character is grappling
    grappling = models.BooleanField(default=False)
    # Whether the character is helpless
    helpless = models.BooleanField(default=False)
    # Whether the character is incorporeal
    incorporeal = models.BooleanField(default=False)
    # Whether the character is invisible
    invisible = models.BooleanField(default=False)
    # Whether the character is nauseated
    nauseated = models.BooleanField(default=False)
    # Whether the character is paralyzed
    paralyzed = models.BooleanField(default=False)
    # Whether the character is petrified
    petrified = models.BooleanField(default=False)
    # Whether the character is pinned
    pinned = models.BooleanField(default=False)
    # Whether the character is prone
    prone = models.BooleanField(default=False)
    # Whether the character is sickened
    sickened = models.BooleanField(default=False)
    # Whether the character is stable
    stable = models.BooleanField(default=False)
    # Whether the character is staggered
    staggered = models.BooleanField(default=False)
    # Whether the character is stunned
    stunned = models.BooleanField(default=False)
    # Whether the character is turned
    turned = models.BooleanField(default=False)
    # Whether the character is unconscious
    unconscious = models.BooleanField(default=False)
    # Whether the character is cowering
    cowering = models.BooleanField(default=False)
    # Whether the character is fatigued 0=normal, 1=fatigued, 2=exhausted
    fatigue_degree = models.IntegerField(null=False, default=0)
    # How much fear 0=normal, 1=shaken, 2=frightened, 3=panicked, 4=cowering
    fear_degree = models.IntegerField(null=False, default=0)

    @cached_property
    def disp_abilities(self):
        return (self.disp_base_str, self.disp_base_dex, self.disp_base_con,
                self.disp_base_int, self.disp_base_wis, self.disp_base_cha)

    @cached_property
    def disp_saves(self):
        return self.disp_base_fort, self.disp_base_ref, self.disp_base_will
        
    # The character's base Str, used in calculations. numeric
    @cached_property
    def base_str(self):
        print('getting base_str')
        return self.base_ability(0)
    
    # The character's base Dex, used in calculations. numeric
    @cached_property
    def base_dex(self):
        return self.base_ability(1)
    
    # The character's base Con, used in calculations. numeric
    @cached_property
    def base_con(self):
        return self.base_ability(2)
    
    # The character's base Int, used in calculations. numeric
    @cached_property
    def base_int(self):
        return self.base_ability(3)
    
    # The character's base Wis, used in calculations. numeric
    @cached_property
    def base_wis(self):
        return self.base_ability(4)
    
    # The character's base Cha, used in calculations. numeric
    @cached_property
    def base_cha(self):
        return self.base_ability(5)
    
    # The character's base Str modifier, calculated from base_str. integer
    @property
    def base_str_mod(self):
        return self.ability_mod(self.base_str)
    
    # The character's base Dex modifier, calculated from base_dex. integer
    @property
    def base_dex_mod(self):
        return self.ability_mod(self.base_dex)
     
    # The character's base Con modifier, calculated from base_con. integer
    @property
    def base_con_mod(self):
        return self.ability_mod(self.base_con)
    
    # The character's base Int modifier, calculated from base_int. integer
    @property
    def base_int_mod(self):
        return self.ability_mod(self.base_int)
    
    # The character's base Wis modifier, calculated from base_wis. integer
    @property
    def base_wis_mod(self):
        return self.ability_mod(self.base_wis)
    
    # The character's base Cha modifier, calculated from base_cha. integer
    @cached_property
    def base_cha_mod(self):
        return self.ability_mod(self.base_cha)

    @cached_property
    def total_ability_bonuses(self):
        return [self.total_ability_bonus(i) for i in range(0, 6)]

    # The character's Str, accounting for all effects. integer
    @cached_property
    def fin_str(self):
        return self.fin_ability(0)
    
    # The character's Dex, accounting for all effects. integer
    @cached_property
    def fin_dex(self):
        return self.fin_ability(1)
    
    # The character's Con, accounting for all effects. integer
    @cached_property
    def fin_con(self):
        return self.fin_ability(2)
    
    # The character's Int, accounting for all effects. integer
    @cached_property
    def fin_int(self):
        return self.fin_ability(3)
    
    # The character's Wis, accounting for all effects. integer
    @cached_property
    def fin_wis(self):
        return self.fin_ability(4)
    
    # The character's Cha, accounting for all effects. integer
    @cached_property
    def fin_cha(self):
        return self.fin_ability(5)
    
    # The character's Str modifier, calculated from fin_str. integer
    @property
    def fin_str_mod(self):
        return self.ability_mod(self.fin_str)
    
    # The character's Dex modifier, calculated from fin_dex. integer
    @property
    def fin_dex_mod(self):
        return self.ability_mod(self.fin_dex)
    
    # The character's Con modifier, calculated from fin_con. integer
    @property
    def fin_con_mod(self):
        return self.ability_mod(self.fin_con)
    
    # The character's Int modifier, calculated from fin_int. integer
    @property
    def fin_int_mod(self):
        return self.ability_mod(self.fin_int)
    
    # The character's Wis modifier, calculated from fin_wis. integer
    @property
    def fin_wis_mod(self):
        return self.ability_mod(self.fin_wis)
    
    # The character's Cha modifier, calculated from fin_cha. integer
    @property
    def fin_cha_mod(self):
        return self.ability_mod(self.fin_cha)

    # The character's base Fortitude save, used in calculations. numeric
    @cached_property
    def base_fort(self):
        return self.base_save(0)

    # The character's base Fortitude save, used in calculations. numeric
    @cached_property
    def base_ref(self):
        return self.base_save(1)

    # The character's base Fortitude save, used in calculations. numeric
    @cached_property
    def base_will(self):
        return self.base_save(2)

    @cached_property
    def fort_ability_mod(self):
        return self.save_ability_mod(0)

    @cached_property
    def ref_ability_mod(self):
        return self.save_ability_mod(1)

    @cached_property
    def will_ability_mod(self):
        return self.save_ability_mod(2)

    @cached_property
    def fort_bonus(self):
        return self.save_bonus(0)

    @cached_property
    def ref_bonus(self):
        return self.save_bonus(1)

    @cached_property
    def will_bonus(self):
        return self.save_bonus(2)

    # The character's base Fortitude save, used in calculations. numeric
    @cached_property
    def fin_fort(self):
        return self.fin_save(0)

    # The character's base Fortitude save, used in calculations. numeric
    @cached_property
    def fin_ref(self):
        return self.fin_save(1)

    # The character's base Fortitude save, used in calculations. numeric
    @cached_property
    def fin_will(self):
        return self.fin_save(2)

    # The character's base Fortitude save, used in calculations. numeric
    @cached_property
    def active_effects(self):
        print('getting active effects')
        raw_effects = list(self.effect_set.filter(active=True))
        feat_effects = []#[f.effect for f in self.feat_set.all()]
        # TODO: Figure out how to implement item properties here.
        item_effects = []
        return (raw_effects + feat_effects +
                item_effects + self.active_conditions)

    @cached_property
    def active_conditions(self):
        conditions = {}
        active = []
        for condition in DEFAULT_CONDITION_EFFECTS:
            try:
                if self._meta.get_field(condition).value_to_string(self) == 'True':
                    active.append(Condition.objects.get(name=condition))
            except (FieldDoesNotExist, ObjectDoesNotExist):
                pass
        if self.fatigue_degree == 1:
            active.append(Condition.objects.get(name='fatigued'))
        elif self.fatigue_degree == 2:
            active.append(Condition.objects.get(name='exhausted'))
        if self.fear_degree == 1:
            active.append(Condition.objects.get(name='shaken'))
        elif self.fear_degree == 2:
            active.append(Condition.objects.get(name='frightened'))
        elif self.fear_degree == 3:
            active.append(Condition.objects.get(name='panicked'))
        return active

    @cached_property
    def all_skills(self):
        skills_unsort = list(self.skill_set.filter(super_skill=None))
        skills_unsort.sort(key=lambda s: s.name)
        skills_sort = []
        for s in skills_unsort:
            sub_skills = list(self.skill_set.filter(super_skill=s))
            sub_skills.sort(key=lambda s: s.name)
            skills_sort.append((s, tuple(sub_skills)))
        return tuple(skills_sort)



    # Parses an ability's display value into a numeric.
    #   ability:
    #       the ability to get bonuses for. integer (see Effect model).
    # Returns a numeric or None. In order of preference, disp_base_X as an
    # integer, disp_base_X as a float, disp_base_X with the first regex
    # indicating a float ('[0-9]+(\.[0-9]+)*'), and None.
    def base_ability(self, ability):
        disp_ability = self.disp_abilities[ability]
        # If we can, just turn it into a numeric
        try:
            return int(disp_ability)
        except ValueError:
            try:
                return float(disp_ability)
            # It doesn't turn into a numeric
            except ValueError:
                # Find the first float-like string in disp_ability
                num_regex = re.compile('[0-9]+(\.[0-9]+)*')
                found = num_regex.search(disp_ability)
                # If it exists
                if found:
                    return float(found.group())
                # If there's something other than a number in disp_ability,
                # treat it as a non-ability.
                else:
                    return None

    # Calculates a final ability score, including all bonuses.
    #   ability:
    #       the ability to get the modifier for. integer (see Effect model).
    # Returns an integer or None.
    def fin_ability(self, ability):
        print('getting final {0}'.format(ability))
        # Start with the base ability
        fin_ability = self.base_ability(ability)
        # If we couldn't parse disp_ability, it's a non-ability
        if fin_ability is None:
            return None
        # Add all penalties and bonuses from effects
        for bonus_type, modifiers in self.total_ability_bonuses[ability].items():
            penalty, bonus = min(modifiers), max(modifiers)
            fin_ability += penalty + bonus
        return fin_ability

    # Gets the ability modifier for an ability. (ability - 10) / 2
    #   ability:
    #       the ability to get the modifier for. integer (see Effect model).
    # Returns an integer or None.
    def ability_mod(self, ability_score):
        try:
            return int((ability_score - 10) / 2)
        # It's not a numeric, so defaults to 0
        except (ValueError, TypeError):
            return 0

    # Parses a save's display value into a numeric.
    #   save:
    #       the save to get bonuses for. integer (see Effect model).
    # Returns a numeric. In order of preference, disp_save as an integer,
    # disp_save as a float, disp_save with the first regex indicating a float
    # ('[0-9]+(\.[0-9]+)*'), and 0.
    def base_save(self, save):
        disp_save = self.disp_saves[save]
        # If we can, just turn it into a numeric
        try:
            return int(disp_save)
        except ValueError:
            try:
                return float(disp_save)
            # It doesn't turn into a numeric easily.
            except ValueError:
                # Find the first float-like string in disp_save
                num_regex = re.compile('[0-9]+(\.[0-9]+)*')
                found = num_regex.search(disp_save)
                # If it exists
                if found:
                    return float(found.group())
                # If there's something other than a number in disp_save
                else:
                    return 0

    def save_ability_mod(self, save):
        return self.ability_mod(self.fin_ability(
            self.ultimate_save_ability(save)))

    def save_bonus(self, save):
        total_bonus = 0
        # Add all bonuses from effects.
        for bonus_type, modifiers in self.total_save_bonus(save).items():
            penalty, bonus = min(modifiers), max(modifiers)
            total_bonus += penalty + bonus
        return total_bonus

    # Gets the final value for a save
    #   save:
    #       the save to get the final value for. integer (see Effect model).
    # Returns an integer.
    def fin_save(self, save):
        # Start with the base save bonus
        fin_save = self.base_save(save)
        # Add the key ability modifier
        fin_save += self.save_ability_mod(save)
        # Add all the bonuses
        fin_save += self.save_bonus(save)
        return fin_save

    # Gets the bonuses and penalties for an ability from a single effect
    #   ability:
    #       the ability to get bonuses for. integer (see Effect model).
    #   effect:
    #       the effect to get bonuses from. Effect.
    # Returns a dictionary. Format is {bonus_type: modifiers}. bonus_type
    # is an integer referring to the bonus type (see models.Effect). modifiers
    # is a range with minimum equal to the penalty of that type (0 if none)
    # and a maximum equal to the bonus of that type (0 if none).
    def effect_ability_bonus(self, ability, effect):
        raw_bonuses = effect.total_ability_bonus(ability)
        # Bonuses are stored as bonus_type: bonus. bonus_type is an integer
        # referring to the bonus types in Effect. bonus is a range with min
        # equal to the worst penalty and a max equal to the best bonus.
        # Remember when setting ranges that the max is set to the second
        # argument _minus one_, so you need to make it one higher.
        bonuses = {}
        for bonus_type, amount in raw_bonuses:
            if bonus_type in bonuses:
                old_bonus = bonuses[bonus_type]
                # If amount is a penalty and worse than the old one, use it
                if amount < min(old_bonus):
                    bonuses[bonus_type] = range(amount, max(old_bonus) + 1)
                # If amount is a bonus and better than the old one, use it
                elif amount > max(old_bonus):
                    bonuses[bonus_type] = range(min(old_bonus), amount + 1)
            else:
                # If amount is a bonus, set penalty to 0 and bonus to amount
                if amount > 0:
                    bonuses[bonus_type] = range(0, amount + 1)
                # If amount is a penalty, set penalty to amount and bonus to 0
                elif amount < 0:
                    bonuses[bonus_type] = range(amount, 1)
                # This shouldn't happen
                else:
                    bonuses[bonus_type] = range(0, 1)
        return bonuses

    # Gets the bonuses and penalties for an ability from a single effect
    #   skill:
    #       the skill to get bonuses for. Skill or integer refering to Skill id.
    #   effect:
    #       the effect to get bonuses from. Effect.
    # Returns a dictionary. Format is {bonus_type: modifiers}. bonus_type
    # is an integer referring to the bonus type (see models.Effect). modifiers
    # is a range with minimum equal to the penalty of that type (0 if none)
    # and a maximum equal to the bonus of that type (0 if none).
    def effect_skill_bonus(self, skill, effect):
        raw_bonuses = effect.total_skill_bonus(skill)
        # Bonuses are stored as bonus_type: bonus. bonus_type is an integer
        # referring to the bonus types in Effect. bonus is a range with min
        # equal to the worst penalty and a max equal to the best bonus.
        # Remember when setting ranges that the max is set to the second
        # argument _minus one_, so you need to make it one higher.
        bonuses = {}
        for bonus_type, amount in raw_bonuses:
            if type(amount) is str:
                amount = {'Strength': self.fin_str_mod,
                          'Dexterity': self.fin_dex_mod,
                          'Constitution': self.fin_con_mod,
                          'Intelligence': self.fin_int_mod,
                          'Wisdom': self.fin_wis_mod,
                          'Charisma': self.fin_cha_mod,
                          }[amount]
            if bonus_type in bonuses:
                old_bonus = bonuses[bonus_type]
                # If amount is a penalty and worse than the old one, use it
                if amount < min(old_bonus):
                    bonuses[bonus_type] = range(amount, max(old_bonus) + 1)
                # If amount is a bonus and better than the old one, use it
                elif amount > max(old_bonus):
                    bonuses[bonus_type] = range(min(old_bonus), amount + 1)
            else:
                # If amount is a bonus, set penalty to 0 and bonus to amount
                if amount > 0:
                    bonuses[bonus_type] = range(0, amount + 1)
                # If amount is a penalty, set penalty to amount and bonus to 0
                elif amount < 0:
                    bonuses[bonus_type] = range(amount, 1)
                # This shouldn't happen
                else:
                    bonuses[bonus_type] = range(0, 1)
        return bonuses

    # Gets the bonuses and penalties for an ability from a single effect
    #   save:
    #       the save to get bonuses for. integer (see Effect model).
    #   effect:
    #       the effect to get bonuses from. Effect.
    # Returns a dictionary. Format is {bonus_type: modifiers}. bonus_type
    # is an integer referring to the bonus type (see models.Effect). modifiers
    # is a range with minimum equal to the penalty of that type (0 if none)
    # and a maximum equal to the bonus of that type (0 if none).
    def effect_save_bonus(self, save, effect):
        raw_bonuses = effect.total_save_bonus(save)
        # Bonuses are stored as bonus_type: bonus. bonus_type is an integer
        # referring to the bonus types in Effect. bonus is a range with min
        # equal to the worst penalty and a max equal to the best bonus.
        # Remember when setting ranges that the max is set to the second
        # argument _minus one_, so you need to make it one higher.
        bonuses = {}
        for bonus_type, amount in raw_bonuses:
            if type(amount) is str:
                amount = {'Strength': self.fin_str_mod,
                          'Dexterity': self.fin_dex_mod,
                          'Constitution': self.fin_con_mod,
                          'Intelligence': self.fin_int_mod,
                          'Wisdom': self.fin_wis_mod,
                          'Charisma': self.fin_cha_mod,
                          }[amount]
            if bonus_type in bonuses:
                old_bonus = bonuses[bonus_type]
                # If amount is a penalty and worse than the old one, use it
                if amount < min(old_bonus):
                    bonuses[bonus_type] = range(amount, max(old_bonus) + 1)
                # If amount is a bonus and better than the old one, use it
                elif amount > max(old_bonus):
                    bonuses[bonus_type] = range(min(old_bonus), amount + 1)
            else:
                # If amount is a bonus, set penalty to 0 and bonus to amount
                if amount > 0:
                    bonuses[bonus_type] = range(0, amount + 1)
                # If amount is a penalty, set penalty to amount and bonus to 0
                elif amount < 0:
                    bonuses[bonus_type] = range(amount, 1)
                # This shouldn't happen
                else:
                    bonuses[bonus_type] = range(0, 1)
        return bonuses

    # Gets the ability bonuses of each type from all effects
    #   ability:
    #       the ability to get bonuses for. integer (see Effect model).
    # Returns a dictionary. Format is {bonus_type: modifiers}. bonus_type
    # is an integer referring to the bonus type (see models.Effect). modifiers
    # is a range with minimum equal to the penalty of that type (0 if none)
    # and a maximum equal to the bonus of that type (0 if none).
    def total_ability_bonus(self, ability):
        print('getting ability bonus for {0}'.format(ability))
        bonuses = {}
        # Cycle through all active effects
        for effect in self.active_effects:
            # Get the ability bonuses for the effect
            # {type: range(penalty, bonus)}
            effect_bonuses = self.effect_ability_bonus(ability, effect)
            # Cycle through each bonus type, adding penalties and bonuses
            for bonus_type in effect_bonuses:
                penalty = min(effect_bonuses[bonus_type])
                bonus = max(effect_bonuses[bonus_type])
                # If we've already had this bonus type from another effect, use
                # the worst penalty and the best bonus.
                if bonus_type in bonuses:
                    old_penalty = min(bonuses[bonus_type])
                    old_bonus = max(bonuses[bonus_type])
                    worst_penalty = min(old_penalty, penalty)
                    best_bonus = max(old_bonus, bonus)
                    bonuses[bonus_type] = range(worst_penalty, best_bonus)
                # If we haven't had this bonus type, just add it to the list
                else:
                    bonuses[bonus_type] = range(penalty, bonus + 1)
        return bonuses

    # Gets the ability bonuses of each type from all effects
    # save:
    #       the save to get bonuses for. integer (see Effect model)
    # Returns a dictionary. Format is {bonus_type: modifiers}. bonus_type
    # is an integer referring to the bonus type (see models.Effect). modifiers
    # is a range with minimum equal to the penalty of that type (0 if none)
    # and a maximum equal to the bonus of that type (0 if none).
    def total_skill_bonus(self, skill):
        bonuses = {}
        # Cycle through all active effects
        for effect in self.active_effects:
            # Get the skill bonuses for the effect {type: range(penalty, bonus)}
            effect_bonuses = self.effect_skill_bonus(skill, effect)
            # Cycle through each bonus type, adding penalties and bonuses
            for bonus_type in effect_bonuses:
                # Penalties and bonuses are stored as ranges.
                penalty = min(effect_bonuses[bonus_type])
                bonus = max(effect_bonuses[bonus_type])
                # If we've already had this bonus type from another effect, use
                # the worst penalty and the best bonus.
                if bonus_type in bonuses:
                    old_penalty = min(bonuses[bonus_type])
                    old_bonus = max(bonuses[bonus_type])
                    worst_penalty = min(old_penalty, penalty)
                    best_bonus = max(old_bonus, bonus)
                    bonuses[bonus_type] = range(worst_penalty, best_bonus)
                # If we haven't had this bonus type, just add it to the list
                else:
                    bonuses[bonus_type] = range(penalty, bonus + 1)
        return bonuses

    # Gets the ability bonuses of each type from all effects
    # save:
    #       the save to get bonuses for. Skill or integer refering to Skill id.
    # Returns a dictionary. Format is {bonus_type: modifiers}. bonus_type
    # is an integer referring to the bonus type (see models.Effect). modifiers
    # is a range with minimum equal to the penalty of that type (0 if none)
    # and a maximum equal to the bonus of that type (0 if none).
    def total_save_bonus(self, save):
        bonuses = {}
        # Cycle through all active effects
        for effect in self.active_effects:
            # Get the save bonuses for the effect {type: range(penalty, bonus)}
            effect_bonuses = self.effect_save_bonus(save, effect)
            # Cycle through each bonus type, adding penalties and bonuses
            for bonus_type in effect_bonuses:
                # Penalties and bonuses are stored as ranges.
                penalty = min(effect_bonuses[bonus_type])
                bonus = max(effect_bonuses[bonus_type])
                # If we've already had this bonus type from another effect, use
                # the worst penalty and the best bonus.
                if bonus_type in bonuses:
                    old_penalty = min(bonuses[bonus_type])
                    old_bonus = max(bonuses[bonus_type])
                    worst_penalty = min(old_penalty, penalty)
                    best_bonus = max(old_bonus, bonus)
                    bonuses[bonus_type] = range(worst_penalty, best_bonus)
                # If we haven't had this bonus type, just add it to the list
                else:
                    bonuses[bonus_type] = range(penalty, bonus + 1)
        return bonuses

    # Determines which ability will be used for a save
    #   save:
    #       the save to get the key ability. integer (see Effect model).
    # Returns an integer indicating the key ability (see Effect model). In order
    # of preference, the ability from the most recently added effect overriding
    # the save ability, the default save ability.
    def ultimate_save_ability(self, save):
        # Get the save override from all effects that have one.
        abilities = [effect.ultimate_save_override(save)
                     for effect in self.active_effects]
        abilities=list(filter((None,None).__ne__, abilities))
        # Get the save override from the most recently added effect.
        try:
            abilities.sort(key=lambda t: t[1])
            return abilities[-1][0]
        # There's no override; get the default
        except (IndexError, TypeError):
            return DEFAULT_SAVE_ABILITIES[save]
