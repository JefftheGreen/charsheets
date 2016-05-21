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
    
        
    # The character's base Str, used in calculations
    @property
    def base_str(self):
        try:
            return max(0, int(self.disp_base_str))
        except:
            try:
                return float(self.disp_base_str)
            except:
                return None
    
    # The character's base Dex, used in calculations
    @property
    def base_dex(self):
        try:
            return int(self.disp_base_dex)
        except:
            try:
                return float(self.disp_base_dex)
            except:
                return None
    
    # The character's base Con, used in calculations
    @property
    def base_con(self):
        try:
            return int(self.disp_base_con)
        except:
            try:
                return float(self.disp_base_con)
            except:
                return None
    
    # The character's base Int, used in calculations
    @property
    def base_int(self):
        try:
            return int(self.disp_base_int)
        except:
            try:
                return float(self.disp_base_int)
            except:
                return None
    
    # The character's base Wis, used in calculations
    @property
    def base_wis(self):
        try:
            return int(self.disp_base_wis)
        except:
            try:
                return float(self.disp_base_wis)
            except:
                return None
    
    # The character's base Cha, used in calculations
    @property
    def base_cha(self):
        try:
            return int(self.disp_base_cha)
        except:
            try:
                return float(self.disp_base_cha)
            except:
                return None
    
    # The character's base Str modifier, calculated from base_str
    @property
    def base_str_mod(self):
        if self.base_str is None:
            return 0
        else:
            return int((self.base_str - 10) / 2)
    
    # The character's base Dex modifier, calculated from base_dex
    @property
    def base_dex_mod(self):
        if self.base_dex is None:
            return 0
        else:
            return int((self.base_dex - 10) / 2)
     
    # The character's base Con modifier, calculated from base_con
    @property
    def base_con_mod(self):
        if self.base_con is None:
            return 0
        else:
            return int((self.base_con - 10) / 2)
    
    # The character's base Int modifier, calculated from base_int
    @property
    def base_int_mod(self):
        if self.base_int is None:
            return 0
        else:
            return int((self.base_int - 10) / 2)
    
    # The character's base Wis modifier, calculated from base_wis
    @property
    def base_wis_mod(self):
        if self.base_wis is None:
            return 0
        else:
            return int((self.base_wis - 10) / 2)
    
    # The character's base Cha modifier, calculated from base_cha
    @property
    def base_cha_mod(self):
        if self.base_cha is None:
            return 0
        else:
            return int((self.base_cha - 10) / 2)
            
    # A 6-tuple of the base abilities for easy reference
    @property
    def base_abilities(self):
        return (self.base_str, self.base_dex, self.base_con,
                self.base_int, self.base_wis, self.base_cha)
    
    # A 6-tuple of the base ability modifiers for easy reference        
    @property
    def base_ability_mods(self):
        return (self.base_str_mod, self.base_dex_mod, self.base_con_mod,
                self.base_int_mod, self.base_wis_mod, self.base_cha_mod)
    
    # The character's Str, accounting for all effects   
    @property
    def fin_str(self):
        fin_str = self.base_str
        for effect in self.effect_set.all():
            pass
        return fin_str
    
    # The character's Dex, accounting for all effects
    @property
    def fin_dex(self):
        fin_dex = self.base_dex
        for effect in self.effect_set.all():
            pass
        return fin_dex
    
    # The character's Con, accounting for all effects
    @property
    def fin_con(self):
        fin_con = self.base_con
        for effect in self.effect_set.all():
            pass
        return fin_con
    
    # The character's Int, accounting for all effects
    @property
    def fin_int(self):
        fin_int = self.base_int
        for effect in self.effect_set.all():
            pass
        return fin_int
    
    # The character's Wis, accounting for all effects
    @property
    def fin_wis(self):
        fin_wis = self.base_wis
        for effect in self.effect_set.all():
            pass
        return fin_wis
    
    # The character's Cha, accounting for all effects
    @property
    def fin_cha(self):
        fin_cha = self.base_cha
        for effect in self.effect_set.all():
            pass
        return fin_cha
    
    # The character's Str modifier, calculated from fin_str
    @property
    def fin_str_mod(self):
        if self.fin_str is None:
            return 0
        else:
            return int((self.fin_str - 10) / 2)
    
    # The character's Dex modifier, calculated from fin_dex
    @property
    def fin_dex_mod(self):
        if self.fin_dex is None:
            return 0
        else:
            return int((self.fin_dex - 10) / 2)
    
    # The character's Con modifier, calculated from fin_con
    @property
    def fin_con_mod(self):
        if self.fin_con is None:
            return 0
        else:
            return int((self.fin_con - 10) / 2)
    
    # The character's Int modifier, calculated from fin_int
    @property
    def fin_int_mod(self):
        if self.fin_int is None:
            return 0
        else:
            return int((self.fin_int - 10) / 2)
    
    # The character's Wis modifier, calculated from fin_wis
    @property
    def fin_wis_mod(self):
        if self.fin_wis is None:
            return 0
        else:
            return int((self.fin_wis - 10) / 2)
    
    # The character's Cha modifier, calculated from fin_cha
    @property
    def fin_cha_mod(self):
        if self.fin_cha is None:
            return 0
        else:
            return int((self.fin_cha - 10) / 2)
    
    # A 6-tuple of the base abilities for easy reference
    @property
    def fin_abilities(self):
        return (self.fin_str, self.fin_dex, self.fin_con,
                self.fin_int, self.fin_wis, self.fin_cha)
    
    # A 6-tuple of the base ability modifiers for easy reference        
    @property
    def fin_ability_mods(self):
        return (self.fin_str_mod, self.fin_dex_mod, self.fin_con_mod,
                self.fin_int_mod, self.fin_wis_mod, self.fin_cha_mod)
                
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