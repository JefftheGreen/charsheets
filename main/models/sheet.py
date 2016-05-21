from django.db import models
from django.contrib.auth.models import User


class Sheet(models.Model):
    
    # The user that created the sheet
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
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
        
    # The character's base Str, used in calculations. integer
    @property
    def base_str(self):
        try:
            return max(0, int(self.disp_base_str))
        except ValueError:
            try:
                return float(self.disp_base_str)
            except ValueError:
                return None
    
    # The character's base Dex, used in calculations. integer
    @property
    def base_dex(self):
        try:
            return int(self.disp_base_dex)
        except ValueError:
            try:
                return float(self.disp_base_dex)
            except ValueError:
                return None
    
    # The character's base Con, used in calculations. integer
    @property
    def base_con(self):
        try:
            return int(self.disp_base_con)
        except ValueError:
            try:
                return float(self.disp_base_con)
            except ValueError:
                return None
    
    # The character's base Int, used in calculations. integer
    @property
    def base_int(self):
        try:
            return int(self.disp_base_int)
        except ValueError:
            try:
                return float(self.disp_base_int)
            except ValueError:
                return None
    
    # The character's base Wis, used in calculations. integer
    @property
    def base_wis(self):
        try:
            return int(self.disp_base_wis)
        except ValueError:
            try:
                return float(self.disp_base_wis)
            except ValueError:
                return None
    
    # The character's base Cha, used in calculations. integer
    @property
    def base_cha(self):
        try:
            return int(self.disp_base_cha)
        except ValueError:
            try:
                return float(self.disp_base_cha)
            except ValueError:
                return None
    
    # The character's base Str modifier, calculated from base_str. integer
    @property
    def base_str_mod(self):
        if self.base_str is None:
            return 0
        else:
            return int((self.base_str - 10) / 2)
    
    # The character's base Dex modifier, calculated from base_dex. integer
    @property
    def base_dex_mod(self):
        if self.base_dex is None:
            return 0
        else:
            return int((self.base_dex - 10) / 2)
     
    # The character's base Con modifier, calculated from base_con. integer
    @property
    def base_con_mod(self):
        if self.base_con is None:
            return 0
        else:
            return int((self.base_con - 10) / 2)
    
    # The character's base Int modifier, calculated from base_int. integer
    @property
    def base_int_mod(self):
        if self.base_int is None:
            return 0
        else:
            return int((self.base_int - 10) / 2)
    
    # The character's base Wis modifier, calculated from base_wis. integer
    @property
    def base_wis_mod(self):
        if self.base_wis is None:
            return 0
        else:
            return int((self.base_wis - 10) / 2)
    
    # The character's base Cha modifier, calculated from base_cha. integer
    @property
    def base_cha_mod(self):
        if self.base_cha is None:
            return 0
        else:
            return int((self.base_cha - 10) / 2)
            
    # All base abilities for easy reference. 6-tuple of integers
    @property
    def base_abilities(self):
        return (self.base_str, self.base_dex, self.base_con,
                self.base_int, self.base_wis, self.base_cha)
    
    # All base ability modifiers for easy reference. 6-tuple of integers
    @property
    def base_ability_mods(self):
        return (self.base_str_mod, self.base_dex_mod, self.base_con_mod,
                self.base_int_mod, self.base_wis_mod, self.base_cha_mod)
    
    # The character's Str, accounting for all effects. integer
    @property
    def fin_str(self):
        fin_str = self.base_str
        if fin_str is None:
            return None
        for bonus_type, modifiers in self.total_ability_bonus(0).items():
            penalty, bonus = min(modifiers), max(modifiers)
            fin_str += penalty + bonus
        return fin_str
    
    # The character's Dex, accounting for all effects. integer
    @property
    def fin_dex(self):
        fin_dex = self.base_dex
        if fin_dex is None:
            return None
        for bonus_type, modifiers in self.total_ability_bonus(1).items():
            penalty, bonus = min(modifiers), max(modifiers)
            fin_dex += penalty + bonus
        return fin_dex
    
    # The character's Con, accounting for all effects. integer
    @property
    def fin_con(self):
        fin_con = self.base_con
        if fin_con is None:
            return None
        for bonus_type, modifiers in self.total_ability_bonus(2).items():
            penalty, bonus = min(modifiers), max(modifiers)
            fin_con += penalty + bonus
        return fin_con
    
    # The character's Int, accounting for all effects. integer
    @property
    def fin_int(self):
        fin_int = self.base_int
        if fin_int is None:
            return None
        for bonus_type, modifiers in self.total_ability_bonus(3).items():
            penalty, bonus = min(modifiers), max(modifiers)
            fin_int += penalty + bonus
        return fin_int
    
    # The character's Wis, accounting for all effects. integer
    @property
    def fin_wis(self):
        fin_wis = self.base_wis
        if fin_wis is None:
            return None
        for bonus_type, modifiers in self.total_ability_bonus(4).items():
            penalty, bonus = min(modifiers), max(modifiers)
            fin_wis += penalty + bonus
        return fin_wis
    
    # The character's Cha, accounting for all effects. integer
    @property
    def fin_cha(self):
        fin_cha = self.base_cha
        if fin_cha is None:
            return None
        for bonus_type, modifiers in self.total_ability_bonus(5).items():
            penalty, bonus = min(modifiers), max(modifiers)
            fin_cha += penalty + bonus
        return fin_cha
    
    # The character's Str modifier, calculated from fin_str. integer
    @property
    def fin_str_mod(self):
        if self.fin_str is None:
            return 0
        else:
            return int((self.fin_str - 10) / 2)
    
    # The character's Dex modifier, calculated from fin_dex. integer
    @property
    def fin_dex_mod(self):
        if self.fin_dex is None:
            return 0
        else:
            return int((self.fin_dex - 10) / 2)
    
    # The character's Con modifier, calculated from fin_con. integer
    @property
    def fin_con_mod(self):
        if self.fin_con is None:
            return 0
        else:
            return int((self.fin_con - 10) / 2)
    
    # The character's Int modifier, calculated from fin_int. integer
    @property
    def fin_int_mod(self):
        if self.fin_int is None:
            return 0
        else:
            return int((self.fin_int - 10) / 2)
    
    # The character's Wis modifier, calculated from fin_wis. integer
    @property
    def fin_wis_mod(self):
        if self.fin_wis is None:
            return 0
        else:
            return int((self.fin_wis - 10) / 2)
    
    # The character's Cha modifier, calculated from fin_cha. integer
    @property
    def fin_cha_mod(self):
        if self.fin_cha is None:
            return 0
        else:
            return int((self.fin_cha - 10) / 2)
    
    # All base abilities for easy reference. 6-tuple of integers
    @property
    def fin_abilities(self):
        return (self.fin_str, self.fin_dex, self.fin_con,
                self.fin_int, self.fin_wis, self.fin_cha)
    
    # All base ability modifiers for easy reference. 6-tuple of integers
    @property
    def fin_ability_mods(self):
        return (self.fin_str_mod, self.fin_dex_mod, self.fin_con_mod,
                self.fin_int_mod, self.fin_wis_mod, self.fin_cha_mod)
    
    @property
    def active_effects(self):
        raw_effects = list(self.effect_set.filter(active=True))
        feat_effects = []#[f.effect for f in self.feat_set.all()]
        # TODO: Figure out how to implement item properties here.
        item_effects = []
        return raw_effects + feat_effects + item_effects

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
    # skill:
    #       the skill to get bonuses for. Skill or integer refering to Skill id.
    # Returns a dictionary. Format is {bonus_type: modifiers}. bonus_type
    # is an integer referring to the bonus type (see models.Effect). modifiers
    # is a range with minimum equal to the penalty of that type (0 if none)
    # and a maximum equal to the bonus of that type (0 if none).
    def total_skill_bonus(self, skill):
        bonuses = {}
        for effect in self.active_effects:
            effect_bonuses = self.effect_ability_bonus(skill, effect)
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