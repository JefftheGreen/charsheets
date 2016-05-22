from django.db import models
    
    
class Container(models.Model):
    
    name = models.CharField(max_length=200)
    max_items = models.IntegerField()
    
    
class Item(models.Model):
    
    WEAPON = 'W'
    ARMOR = 'A'
    SHIELD = 'S'
    CLOTHING = 'C'
    TOOL = 'T'
    
    TYPE_CHOICES = (
                    (WEAPON, 'Weapon'),
                    (ARMOR, 'Armor'),
                    (SHIELD, 'Shield'),
                    (CLOTHING, 'Clothing'),
                    (TOOL, 'Tool'))
    
    name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=1, choices=TYPE_CHOICES,
                                 default=TOOL)
    damage = models.CharField(max_length=50)
    critical = models.CharField(max_length=50)
    weapon_range = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    damage_type = models.CharField(max_length=50)
    base_ac_bonus = models.IntegerField(max_length=50)
    base_acp = models.CharField(max_length=50)
    base_asf = models.CharField(max_length=50)
    weapon_enhancement_bonus = models.CharField(max_length=50)
    armor_enhancement_bonus = models.CharField(max_length=50)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)


class Property(models.Model):
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
            
class Skill(models.Model):
    
    # Value keys for the abilities
    STR = 0
    DEX = 1
    CON = 2
    INT = 3
    WIS = 4
    CHA = 5
    
    ABILITY_CHOICES = (
                       (STR, 'Strength'),
                       (DEX, 'Dexterity'),
                       (CON, 'Constitution'),
                       (INT, 'Intelligence'),
                       (WIS, 'Wisdom'),
                       (CHA, 'Charisma')
                       )
    
    name = models.CharField(max_length=200)
    default_stat = models.IntegerField(default=None, null=True, 
                                       choices=ABILITY_CHOICES)
    sheet = models.ForeignKey('Sheet', null=True, default=None)
    super_skill = models.ForeignKey('self', null=True, default=None)
    ranks = models.IntegerField(default=0)
    misc_mod = models.IntegerField(default=0)
    acp = models.IntegerField(default=0)
    rename = models.BooleanField(default=True)
    stat_override = models.IntegerField(default=None, null=True, 
                                        choices=ABILITY_CHOICES)

    def __str__(self):
        return self.name

   
# Class representing feats. Mostly a wrapper for Effect, but stores its own
# description and name.
class Feat(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    effect = models.ForeignKey('Effect', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name


# Class representing racial abilities. Mostly a wrapper for Effect, but stores 
# its own description and name. 
class RacialAbility(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    effect = models.ForeignKey('Effect', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name


# Class representing class abilities. Mostly a wrapper for Effect, but stores 
# its own description and name. 
class ClassAbility(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    effect = models.ForeignKey('Effect', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
