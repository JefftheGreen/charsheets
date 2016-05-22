from django.test import TestCase
from main.models import Effect, Sheet, Skill
from main.default_data import main


class Effect_Test(TestCase):
    
    def setUp(self):
        main()
        sheet = Sheet(owner_id=0, disp_base_str='10', disp_base_dex='12',
                      disp_base_con='14', disp_base_int='16',
                      disp_base_wis='18', disp_base_cha='20',
                      name='test_sheet')
        sheet.save()
        supes = Effect(owner_id=0, skill_bonus_id=10, bonus_amount=2, 
                       bonus_type=0, name='test_sub_effects', sheet=sheet)
        supes.save()
        supes2 = Effect(owner_id=0, skill_bonus_id=10, bonus_amount=2,
                        bonus_type=0, name='test_sub_effects2', sheet=sheet,
                        active=False)
        supes2.save()
        sub = Effect(owner_id=0, skill_bonus_id=11, bonus_amount=5, 
                     bonus_type=1, parent_effect=supes)
        sub2 = Effect(owner_id=0, skill_bonus_id=11, from_x_stat=3,
                      bonus_type=2, parent_effect=supes)
        sub3 = Effect(owner_id=0, ability_bonus=0, bonus_amount=10,
                      bonus_type=2, parent_effect=supes)
        sub4 = Effect(owner_id=0, ability_bonus=0, bonus_amount=2,
                      bonus_type=5, parent_effect=supes)
        sub5 = Effect(owner_id=0, ability_bonus=0, bonus_amount=6,
                      bonus_type=2, parent_effect=supes)
        sub.save()
        sub2.save()
        sub3.save()
        sub4.save()
        sub5.save()
                      
    def test_sub_effects(self):
        supes = Effect.objects.get(name='test_sub_effects')
        assert supes.skill_bonuses == {
            10: {0:[2]},
            11: {1:[5], 2:['Intelligence']},
        }

    def test_effects(self):
        sheet = Sheet.objects.get(name='test_sheet')
        effect = Effect.objects.get(name='test_sub_effects')
        skill = Skill.objects.get(id=11)
        print(sheet.effect_set.all(), sheet.effect_set.filter(active=True))
        print('str', sheet.fin_str)
