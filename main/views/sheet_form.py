from django import forms
from main.models import Sheet


class SheetForm(forms.ModelForm):

    ABILITIES = ['str', 'dex', 'con', 'int', 'wis', 'cha']
    SAVES = ['fort', 'ref', 'will']

    class Meta:
        model = Sheet
        fields = [#'char_name', 'race', 'classes', 'gender', 'alignment',
                  #'deity', 'campaign', 'age', 'disp_size', 'disp_base_str',
                  'disp_base_str',
                  'disp_base_dex', 'disp_base_con', 'disp_base_int',
                  'disp_base_wis', 'disp_base_cha'] #'disp_base_fort',
                  #'disp_base_ref','disp_base_will', 'blinded', 'confused',
                  #'dazed', 'dazzled', 'deafened', 'disabled', 'dying',
                  #'entangled', 'fascinated', 'flat_footed', 'grappling',
                  #'helpless', 'incorporeal', 'invisible', 'nauseated',
                  #'paralyzed', 'petrified', 'pinned', 'prone', 'sickened',
                  #'stable', 'staggered', 'stunned', 'turned', 'unconscious']