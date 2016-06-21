from django.db import models
    
    
class Container(models.Model):

    # The container's name. This is displayed on the sheet.
    name = models.CharField(max_length=200)
    # The maximum number of items that can be contained in the container.
    max_items = models.IntegerField(null=True, default=None)
    # If true, the contents do not count against encumbrance.
    weightless = models.BooleanField(default=False)
    # The weight of the container itself, factored into encumbrance.
    weight = models.FloatField(null=True, default=None)
    
    
class Item(models.Model):

    # Value keys for the item types.
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

    # The item's name. This is displayed on the sheet.
    name = models.CharField(max_length=200)
    # The type of item. Determines what fields are available and considered.
    item_type = models.CharField(max_length=1, choices=TYPE_CHOICES,
                                 default=TOOL)
    # The damage a weapon does. This is displayed on the sheet.
    damage = models.CharField(max_length=50)
    # The type of critical a weapon does. This is displayed on the sheet.
    critical = models.CharField(max_length=50)
    # The weapon's range. This is displayed on the sheet.
    weapon_range = models.CharField(max_length=50)
    # The weight of the weapon, parsed and factored into encumbrance.
    weight_disp = models.CharField(max_length=50)
    # The size of the item. This is displayed on the sheet.
    size = models.CharField(max_length=50)
    # The damage type the weapon does. This is displayed on the sheet.
    damage_type = models.CharField(max_length=50)
    # The base AC bonus of armor or shield, parsed and factored into AC.
    base_ac_disp = models.CharField(max_length=50)
    # The base armor check penalty of armor or shield, parsed and factored
    # into ACP.
    base_acp_disp = models.CharField(max_length=50)
    # The base arcane spell failure of armor or shield, parsed and factored
    # into ASF
    base_asf_disp = models.CharField(max_length=50)
    # The enhancement bonus of the weapon.
    weapon_enhancement_bonus = models.CharField(max_length=50)
    # The enhancement bonus of the armor.
    armor_enhancement_bonus = models.CharField(max_length=50)
    # The container the item is in.
    container = models.ForeignKey(Container, on_delete=models.CASCADE)


class Property(models.Model):

    # The item the property is attached to.
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # The effect the property bestows on the item.
    effect = models.ForeignKey('Effect', null=True, default=None,
                               on_delete=models.SET_NULL)
    
            
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

    # The name of the skill, displayed on the sheet.
    name = models.CharField(max_length=200)
    # The default key ability for the skill.
    default_stat = models.IntegerField(default=None, null=True, 
                                       choices=ABILITY_CHOICES)
    # The sheet that the skill is attached to.
    sheet = models.ForeignKey('Sheet', null=True, default=None)
    # Some skills have a super skill that is used for visual grouping and
    # controlling default behavior. For example, Perform for Perform (dance) or
    # Knowledge for Knowledge (arcana)
    super_skill = models.ForeignKey('self', null=True, default=None)
    # The ranks the character has in the skill
    ranks = models.FloatField(default=0)
    # Any miscellaneous modifier not attached to the
    misc_mod_disp = models.CharField(max_length=200, default='')
    # The multiplier for armor check penalty. Usually 0 or 1, sometimes higher.
    acp = models.IntegerField(default=0)
    # Is the user allowed to rename the skill.
    rename = models.BooleanField(default=True)
    # Manual override of the key stat. This is used first, then any from
    # effects, then the default key stat.
    stat_override = models.IntegerField(default=None, null=True, 
                                        choices=ABILITY_CHOICES)

    def __str__(self):
        return self.name

   
# Class representing feats. Mostly a wrapper for Effect, but stores its own
# description and name.
class Feat(models.Model):

    # The name of the feat, displayed on the sheet.
    name = models.CharField(max_length=200)
    # The description of the feat, displayed on the sheet.
    description = models.CharField(max_length=1000)
    # The effect the feat grants.
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
