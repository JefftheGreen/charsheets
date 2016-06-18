# Value keys for the abilities
STR = 0
DEX = 1
CON = 2
INT = 3
WIS = 4
CHA = 5

# Value keys for bonus types
ALC = 0
Arm = 1
CRC = 2
CMP = 3
DEF = 4
DIV = 5
DDG = 6
ENH = 7
EXL = 8
INS = 9
LCK = 10
MRL = 11
NAT = 12
PRF = 13
RAC = 14
RES = 15
SAC = 16
SHD = 17
UNT = 18

SKILL_DEFAULTS_3_5 = ("Appraise", "Autohypnosis", "Balance", "Bluff", "Climb", 
                      "Concentration", "Craft", "Decipher Script", "Diplomacy", 
                      "Disable Device", "Disguise", "Escape Artist", 
                      "Gather Information", "Handle Animal", "Heal", "Hide", 
                      "Intimidate", "Jump", "Knowledge", "Listen", 
                      "Lucid Dreaming",  "Martial Lore", "Move Silently", 
                      "Open Lock", "Perform", "Profession", "Forgery", "Psicraft", 
                      "Ride", "Search", "Sense Motive",  "Sleight Of Hand", 
                      "Speak Language", "Spellcraft", "Spot", "Survival", "Swim", 
                      "Tumble", "Use Magic Device", "Use Psionic Device",
                      "Use Rope")
    
SKILL_DEFAULT_ABIlitiES_3_5 = {"Appraise": INT,
                               "Autohypnosis": WIS, 
                               "Balance": DEX, 
                               "Bluff": CHA, 
                               "Climb": STR, 
                               "Concentration": CON, 
                               "Craft": INT, 
                               "Decipher Script": INT, 
                               "Diplomacy": CHA, 
                               "Disable Device": INT,
                               "Disguise": CHA, 
                               "Escape Artist": DEX, 
                               "Gather Information": CHA, 
                               "Handle Animal": CHA, 
                               "Heal": WIS, 
                               "Hide": DEX, 
                               "Intimidate": CHA, 
                               "Jump": STR, 
                               "Knowledge": INT,
                               "Listen": WIS,
                               "Lucid Dreaming": WIS, 
                               "Martial Lore": INT, 
                               "Move Silently": DEX, 
                               "Open Lock": DEX, 
                               "Perform": CHA, 
                               "Profession": WIS, 
                               "Forgery": INT, 
                               "Psicraft": INT, 
                               "Ride": DEX, 
                               "Search": INT,
                               "Sense Motive": WIS,  
                               "Sleight Of Hand": DEX, 
                               "Speak Language": None, 
                               "Spellcraft": INT, 
                               "Spot": WIS, 
                               "Survival": WIS, 
                               "Swim": STR, 
                               "Tumble": DEX, 
                               "Use Magic Device": CHA, 
                               "Use Psionic Device": CHA,
                               "Use Rope": DEX}
                             
SUBSKILLS = {"Craft": ["alchemy", "armorsmithing", "bowmaking", 
                       "poisonmaking" "trapmaking", "weaponsmithing"],
             "Knowledge": ["arcana", "architecture and engineering",
                           "dungeoneering", "geography", "history",
                           "local", "nature", "nobility and royalty",
                           "psionics", "religion", "the planes"],
             "Perform": ["Act","Comedy", "Dance", "Keyboard instruments",
                         "Oratory", "Percussion instruments", 
                         "String instruments", "Wind instruments", "Sing"]}
                         
SKILL_ACP = {"Appraise": 0,
             "Autohypnosis": 0,
             "Balance": 1, 
             "Bluff": 0, 
             "Climb": 1, 
             "Concentration": 0,
             "Craft": 0, 
             "Decipher Script": 0,
             "Diplomacy": 0, 
             "Disable Device": 0,
             "Disguise": 0, 
             "Escape Artist": 1, 
             "Gather Information": 0, 
             "Handle Animal": 0, 
             "Heal": 0, 
             "Hide": 1, 
             "Intimidate": 0, 
             "Jump": 1, 
             "Knowledge": 0,
             "Listen": 0,
             "Lucid Dreaming": 0, 
             "Martial Lore": 0, 
             "Move Silently": 1, 
             "Open Lock": 0, 
             "Perform": 0, 
             "Profession": 0, 
             "Forgery": 0, 
             "Psicraft": 0, 
             "Ride": 0, 
             "Search": 0,
             "Sense Motive": 0, 
             "Sleight Of Hand": 1, 
             "Speak Language": 0,
             "Spellcraft": 0, 
             "Spot": 0, 
             "Survival": 0, 
             "Swim": 2, 
             "Tumble": 1, 
             "Use Magic Device": 0, 
             "Use Psionic Device": 0,
             "Use Rope": 0}
             
DEFAULT_SKILL_IDS = range(1, 55)

DEFAULT_SAVE_ABILITIES = {0: 2,
                          1: 1,
                          2: 4}

BONUS_TYPE_CHOICES = (
    (ALC, 'Alchemical'),
    (Arm, 'Armor'),
    (CRC, 'Circumstance'),
    (CMP, 'Competence'),
    (DEF, 'Deflection'),
    (DIV, 'Divine'),
    (DDG, 'Dodge'),
    (ENH, 'Enhancement'),
    (EXL, 'Exalted'),
    (INS, 'Insight'),
    (LCK, 'Luck'),
    (MRL, 'Morale'),
    (NAT, 'Natural'),
    (PRF, 'Profane'),
    (RAC, 'Racial'),
    (RES, 'Resistance'),
    (SAC, 'Sacred'),
    (SHD, 'Shield'),
    (UNT, 'Untyped/Other')
)

# Value keys for the saves
FORT = 0
REF = 1
WILL = 2

# Value keys for the abilities
STR = 0
DEX = 1
CON = 2
INT = 3
WIS = 4
CHA = 5

SAVE_CHOICES = (
    (FORT, "Fortitude"),
    (REF, "Reflex"),
    (WILL, "Will")
)

ABILITY_CHOICES = (
    (STR, 'Strength'),
    (DEX, 'Dexterity'),
    (CON, 'Constitution'),
    (INT, 'Intelligence'),
    (WIS, 'Wisdom'),
    (CHA, 'Charisma')
)

DEFAULT_CONDITION_EFFECTS = {'blinded': (('ac', -2),
                                         ('no dex to ac', True),
                                         ('skill', ('Search', -4)),
                                         ('ability skill', (0, -4)),
                                         ('ability skill', (1, -4))),
                             'cowering': (('ac', -2),
                                          ('no dex to ac', True)),
                             'dazzled': (('attack', -1),
                                         ('skill', ('Search', -1)),
                                         ('skill', ('Spot', -1))),
                             'deafened': (('initiative', -4),),
                             'entangled': (('attack', -2),
                                           ('ability', (1, -4))),
                             'exhausted': (('ability', (0, -6)),
                                           ('ability', (1, -6))),
                             'fatigued': (('ability', (0, -2)),
                                          ('ability', (1, -2))),
                             'flat-footed': (('no dex to ac', True),),
                             'frightened': (('attack', -2),
                                            ('save', (0, -2)),
                                            ('save', (1, -2)),
                                            ('save', (2, -2)),
                                            ('skill', ('all', -2))),
                             'grappling': (('no dex to ac', True),),
                             'helpless': (('ability equals', (1, 0)),),
                             'panicked': (('attack', -2),
                                          ('save', (0, -2)),
                                          ('save', (1, -2)),
                                          ('save', (2, -2)),
                                          ('skill', ('all', -2))),
                             'paralyzed': (('ability equals', (0, 0)),
                                           ('ability equals', (1, 0))),
                             'petrified': (('ability equals', (1, 0)),),
                             'prone': (('melee', -4),),
                             'shaken': (('attack', -2),
                                        ('save', (0, -2)),
                                        ('save', (1, -2)),
                                        ('save', (2, -2)),
                                        ('skill', ('all', -2))),
                             'sickened': (('attack', -2),
                                          ('save', (0, -2)),
                                          ('save', (1, -2)),
                                          ('save', (2, -2)),
                                          ('skill', ('all', -2))),
                             'stunned': (('ac', -2),
                                         ('no dex to ac', True)),
                             'unconscious': (('ability equals', (1, 0)),)}


def create_default_skills():
    from .models import Skill
    skill_id = 1
    for s in SKILL_DEFAULTS_3_5:
        ability = SKILL_DEFAULT_ABIlitiES_3_5[s]
        acp = SKILL_ACP[s]
        skill = Skill(id=skill_id, rename=False, acp=acp, 
                      default_stat=ability, name=s)
        skill.save()
        skill_id += 1
        if s == "Knowledge":
            for ss in SUBSKILLS[s]:
                sub_skill = Skill(rename=False, acp=acp, default_stat=ability,
                                  name=ss, super_skill=skill, id=skill_id)
                sub_skill.save()
                skill_id += 1


def create_conditions():
    from .models import Condition
    import warnings
    condition_id = 1
    for condition in DEFAULT_CONDITION_EFFECTS:
        c = Condition(id=condition_id, name=condition)
        c.save()
        condition_id += 1
    for condition in DEFAULT_CONDITION_EFFECTS:
        for effect, value in DEFAULT_CONDITION_EFFECTS[condition]:
            if effect == 'ac':
                c = Condition(parent_effect=
                                Condition.objects.get(name=condition),
                              ac_bonus=True, bonus_amount=value)
                c.save()
            elif effect == 'no dex to ac':
                c = Condition(parent_effect=
                              Condition.objects.get(name=condition),
                              no_dex_to_ac=True)
                c.save()
            elif effect == 'skill':
                c = Condition(parent_effect=
                              Condition.objects.get(name=condition),
                              skill_bonus=value[0], bonus_amount=value[1])
                c.save()
            elif effect == 'ability skill':
                c = Condition(parent_effect=
                              Condition.objects.get(name=condition),
                              ability_skill_bonus=value[0],
                              bonus_amount=value[1])
                c.save()
            elif effect == 'attack':
                c = Condition(parent_effect=
                              Condition.objects.get(name=condition),
                              attack_bonus=2, bonus_amount=value)
                c.save()
            elif effect == 'initiative':
                c = Condition(parent_effect=
                              Condition.objects.get(name=condition),
                              initiative_bonus=True, bonus_amount=value)
                c.save()
            elif effect == 'ability equals':
                c = Condition(parent_effect=
                              Condition.objects.get(name=condition),
                              ability_set=value[0], bonus_amount=value[1])
                c.save()
            elif effect == 'ability':
                c = Condition(parent_effect=
                              Condition.objects.get(name=condition),
                              ability_bonus=value[0], bonus_amount=value[1])
                c.save()
            elif effect == 'melee':
                c = Condition(parent_effect=
                              Condition.objects.get(name=condition),
                              attack_bonus=0, bonus_amount=value)
                c.save()
            elif effect == 'save':
                c = Condition(parent_effect=
                              Condition.objects.get(name=condition),
                              save_bonus=value[0], bonus_amount=value[1])
                c.save()
            else:
                w = ("Condition {0} has an unrecognized effect"
                     .format(condition))
                warnings.warn(w, RuntimeWarning)