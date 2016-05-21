# Value keys for the abilities
STR = 0
DEX = 1
CON = 2
INT = 3
WIS = 4
CHA = 5

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

def main():
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