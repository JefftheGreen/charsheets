from django import forms
from main.models import Sheet


class SheetForm(forms.ModelForm):

    ABILITIES = ['str', 'dex', 'con', 'int', 'wis', 'cha']
    SAVES = ['fort', 'ref', 'will']
    UNGROUPED_CONDITIONS = ['blinded', 'confused', 'dazed', 'dazzled',
                            'deafened', 'disabled', 'dying', 'entangled',
                            'fascinated', 'flat_footed', 'grappling',
                            'helpless', 'incorporeal', 'invisible', 'nauseated',
                            'paralyzed', 'petrified', 'pinned', 'prone',
                            'sickened', 'stable', 'staggered', 'stunned',
                            'turned', 'unconscious']
    CONDITION_GROUPS =[('Fear', ['shaken', 'frightened', 'panicked',
                                 'cowering']),
                       ('Fatigue', ['fatigued', 'exhausted'])]

    fatigued = forms.BooleanField(required=False)
    exhausted = forms.BooleanField(required=False)
    shaken = forms.BooleanField(required=False)
    frightened = forms.BooleanField(required=False)
    panicked = forms.BooleanField(required=False)

    class Meta:
        model = Sheet
        fields = [#'char_name', 'race', 'classes', 'gender', 'alignment',
                  #'deity', 'campaign', 'age', 'disp_size',
                  'disp_base_str',
                  'disp_base_dex', 'disp_base_con', 'disp_base_int',
                  'disp_base_wis', 'disp_base_cha', 'disp_base_fort',
                  'disp_base_ref', 'disp_base_will', 'blinded', 'confused',
                  'dazed', 'dazzled', 'deafened', 'disabled', 'dying',
                  'entangled', 'fascinated', 'flat_footed', 'grappling',
                  'helpless', 'incorporeal', 'invisible', 'nauseated',
                  'paralyzed', 'petrified', 'pinned', 'prone', 'sickened',
                  'stable', 'staggered', 'stunned', 'turned', 'unconscious', 'cowering']


    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            sheet = kwargs['instance']
            initial = kwargs.get('initial', {})
            initial['fatigued'] = sheet.fatigue_degree == 1
            initial['exhausted'] = sheet.fatigue_degree == 2
            initial['shaken'] = sheet.fear_degree == 1
            initial['frightened'] = sheet.fear_degree == 2
            initial['panicked'] = sheet.fear_degree == 3
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    @property
    def fatigue_degree(self):
        return (2 if self['exhausted'].value()
                else 1 if self['fatigued'].value() else 0)

    @property
    def fear_degree(self):
        return (3 if self['panicked'].value()
                else 2 if self['frightened'].value()
                else 1 if self['shaken'].value() else 0)

    @property
    def condition_groups(self):
        return [(title, [self[c] for c in cs])
                for title, cs in self.CONDITION_GROUPS]

    def save(self, *args, **kwargs):
        self.instance.fatigue_degree = self.fatigue_degree
        self.instance.fear_degree = self.fear_degree
        self.instance.save()
        super().save(*args, **kwargs)