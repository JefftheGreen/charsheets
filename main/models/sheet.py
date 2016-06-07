from django.db import models
from django.contrib.auth.models import User
import re


class Sheet(models.Model):

    SAVE_ABILITIES = {0: 2,
                      1: 1,
                      2: 4}
    
    # The user that created the sheet
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # The time the effect was created
    date = models.DateTimeField(default=datetime.now)
    # The name of the sheet, displayed where the sheet is referred to
    name = models.CharField(max_length=200)
    # The character name, displayed on the sheet
    char_name = models.CharField(max_length=200)
    # The character race, displayed on the sheet
    race = models.CharField(max_length=200)
    # The character classes, displayed on the sheet
    classes = models.CharField(max_length=200)
    # The character's gender, displayed on the sheet
    gender = models.CharField(max_length=200)
    # The character's alignment, displayed on the sheet
    alignment = models.CharField(max_length=200)
    # The character's deity, displayed on the sheet
    deity = models.CharField(max_length=200)
    # The campaign the character is for, displayed on the sheet
    campaign = models.CharField(max_length=200)
    # The character's age, displayed on the sheet
    age = models.CharField(max_length=200)
    # The character's size, displayed on the sheet, and parsed for calculations
    _size = models.CharField(max_length=200)
    # The character's Str, displayed on the sheet, and parsed for calculations
    disp_base_str = models.CharField(max_length=5)
    # The character's Dex, displayed on the sheet, and parsed for calculations
    disp_base_dex = models.CharField(max_length=5)
    # The character's Con, displayed on the sheet, and parsed for calculations
    disp_base_con = models.CharField(max_length=5)
    # The character's Int, displayed on the sheet, and parsed for calculations
    disp_base_int = models.CharField(max_length=5)
    # The character's Wis, displayed on the sheet, and parsed for calculations
    disp_base_wis = models.CharField(max_length=5)
    # The character's Cha, displayed on the sheet, and parsed for calculations
    disp_base_cha = models.CharField(max_length=5)
    # The character's Will, displayed on the sheet, and parsed for calculations
    disp_base_will = models.CharField(max_length=5)
    # The character's Ref, displayed on the sheet, and parsed for calculations
    disp_base_ref = models.CharField(max_length=5)
    # The character's Fort, displayed on the sheet, and parsed for calculations
    disp_base_fort = models.CharField(max_length=5)
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
    # Whether the character is fatigued 0=normal, 1=fatigued, 2=exhausted
    fatigue_degree = models.IntegerField(null=False, default=0)
    # How much fear 0=normal, 1=shaken, 2=frightened, 3=panicked, 4=cowering
    fear_degree = models.IntegerField(null=False, default=0)

    @property
    def disp_abilities(self):
        return (self.disp_base_str, self.disp_base_dex, self.disp_base_con,
                self.disp_base_int, self.disp_base_wis, self.disp_base_cha)

    @property
    def disp_saves(self):
        return (self.disp_base_fort, self.disp_base_ref, self.disp_base_will)
        
    # The character's base Str, used in calculations. integer
    @property
    def base_str(self):
        return self.base_ability(0)
    
    # The character's base Dex, used in calculations. integer
    @property
    def base_dex(self):
        return self.base_ability(1)
    
    # The character's base Con, used in calculations. integer
    @property
    def base_con(self):
        return self.base_ability(2)
    
    # The character's base Int, used in calculations. integer
    @property
    def base_int(self):
        return self.base_ability(3)
    
    # The character's base Wis, used in calculations. integer
    @property
    def base_wis(self):
        return self.base_ability(4)
    
    # The character's base Cha, used in calculations. integer
    @property
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
    @property
    def base_cha_mod(self):
        return self.ability_mod(self.base_cha)
    
    # The character's Str, accounting for all effects. integer
    @property
    def fin_str(self):
        fin_str = self.fin_ability(0)
        # Apply fatigue/exhaustion penalties
        fin_str += [0, -2, -6][self.fatigue_degree]
        fin_str = 0 if self.paralyzed else fin_str
        return fin_str
    
    # The character's Dex, accounting for all effects. integer
    @property
    def fin_dex(self):
        fin_dex = self.fin_ability(1)
        # Apply fatigue/exhaustion penalties
        fin_dex += [0, -2, -6][self.fatigue_degree]
        fin_dex = 0 if self.paralyzed or self.helpless else fin_dex
        return fin_dex
    
    # The character's Con, accounting for all effects. integer
    @property
    def fin_con(self):
        return self.fin_ability(2)
    
    # The character's Int, accounting for all effects. integer
    @property
    def fin_int(self):
        return self.fin_ability(3)
    
    # The character's Wis, accounting for all effects. integer
    @property
    def fin_wis(self):
        return self.fin_ability(4)
    
    # The character's Cha, accounting for all effects. integer
    @property
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
    
    @property
    def active_effects(self):
        raw_effects = list(self.effect_set.filter(active=True))
        feat_effects = []#[f.effect for f in self.feat_set.all()]
        # TODO: Figure out how to implement item properties here.
        item_effects = []
        return raw_effects + feat_effects + item_effects

    @property
    def base_fort(self):
        num_regex = re.compile('[0-9]+')
        found = num_regex.search(self.disp_base_fort)
        if found:
            return found.group()
        else:
            return 0

    @property
    def base_ref(self):
        num_regex = re.compile('[0-9]+')
        found = num_regex.search(self.disp_base_ref)
        if found:
            return found.group()
        else:
            return 0

    @property
    def base_will(self):
        num_regex = re.compile('[0-9]+')
        found = num_regex.search(self.disp_base_will)
        if found:
            return found.group()
        else:
            return 0

    @property
    def fin_fort(self):
        return self.fin_save(0)

    @property
    def fin_ref(self):
        return self.fin_save(1)

    @property
    def fin_will(self):
        return self.fin_save(2)

    def base_ability(self, ability):
        disp_ability = self.disp_abilities[ability]
        try:
            return int(disp_ability)
        except ValueError:
            try:
                return float(disp_ability)
            except ValueError:
                num_regex = re.compile('[0-9]+')
                found = num_regex.search(disp_ability)
                if found:
                    return int(found.group())
                else:
                    return None

    def fin_ability(self, ability):
        fin_ability = self.base_ability(ability)
        if fin_ability is None:
            return None
        for bonus_type, modifiers in self.total_ability_bonus(ability).items():
            penalty, bonus = min(modifiers), max(modifiers)
            fin_ability += penalty + bonus
        return fin_ability


    def ability_mod(self, ability_score):
        try:
            return int((ability_score - 10) / 2)
        except (ValueError, TypeError):
            return None

    def base_save(self, save):
        disp_save = self.disp_saves[save]
        try:
            return int(disp_save)
        except ValueError:
            try:
                return float(disp_save)
            except ValueError:
                num_regex = re.compile('[0-9]+')
                found = num_regex.search(disp_save)
                if found:
                    return int(found.group())
                else:
                    return None

    def fin_save(self, save):
        fin_save = self.base_save(save)
        fin_save += self.fin_ability(self.ultimate_save_ability(save))
        for bonus_type, modifiers in self.total_save_bonus(save).items():
            penalty, bonus = min(modifiers), max(modifiers)
            fin_save += penalty + bonus
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
        bonuses = {}
        for effect in self.active_effects:
            effect_bonuses = self.effect_ability_bonus(ability, effect)
            for bonus_type in effect_bonuses:
                penalty = min(effect_bonuses[bonus_type])
                bonus = max(effect_bonuses[bonus_type])
                if bonus_type in bonuses:
                    old_penalty = min(bonuses[bonus_type])
                    old_bonus = max(bonuses[bonus_type])
                    worst_penalty = min(old_penalty, penalty)
                    best_bonus = max(old_bonus, bonus)
                    bonuses[bonus_type] = range(worst_penalty, best_bonus)
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
        for effect in self.active_effects:
            effect_bonuses = self.effect_skill_bonus(skill, effect)
            for bonus_type in effect_bonuses:
                penalty = min(effect_bonuses[bonus_type])
                bonus = max(effect_bonuses[bonus_type])
                if bonus_type in bonuses:
                    old_penalty = min(bonuses[bonus_type])
                    old_bonus = max(bonuses[bonus_type])
                    worst_penalty = min(old_penalty, penalty)
                    best_bonus = max(old_bonus, bonus)
                    bonuses[bonus_type] = range(worst_penalty, best_bonus)
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
        for effect in self.active_effects:
            effect_bonuses = self.effect_save_bonus(save, effect)
            for bonus_type in effect_bonuses:
                penalty = min(effect_bonuses[bonus_type])
                bonus = max(effect_bonuses[bonus_type])
                if bonus_type in bonuses:
                    old_penalty = min(bonuses[bonus_type])
                    old_bonus = max(bonuses[bonus_type])
                    worst_penalty = min(old_penalty, penalty)
                    best_bonus = max(old_bonus, bonus)
                    bonuses[bonus_type] = range(worst_penalty, best_bonus)
                else:
                    bonuses[bonus_type] = range(penalty, bonus + 1)
        return bonuses

    def ultimate_save_ability(self, save):
        abilities = [effect.ultimate_save_override(save)
                     for effect in self.active_effects]
        if abilities:
            abilities.sort(key=lambda t: t[1])
            return abilities[-1][0]
        else:
            return self.SAVE_ABILITIES[save]
