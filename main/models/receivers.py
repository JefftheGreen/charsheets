from django.db.models.signals import post_save
from django.dispatch import receiver
from main.default_data import DEFAULT_SKILL_IDS
from . import Sheet
from .misc import Skill

@receiver(post_save)
def finished_saving(sender, **kwargs):
    if sender == Sheet:
        try:
            created = kwargs['created']
            instance = kwargs['instance']
            skill_ids = {None:None}
            if created:
                # Loop through skills that aren't subskills
                for skill in Skill.objects.filter(id__in=DEFAULT_SKILL_IDS):
                    old_id = skill.id
                    # Remove 
                    skill.pk = None
                    skill.sheet = instance
                    skill.save()
                    skill_ids[old_id] = skill.id
                for sub_skill in (Skill.objects.filter
                                      (id__in=skill_ids.values())
                                       .exclude(super_skill=None)):
                    sub_skill.super_skill_id = skill_ids[sub_skill
                                                         .super_skill.id]
                    sub_skill.save()
        except KeyError:
            print('finished_saving did not receive expected kwargs')
            raise
