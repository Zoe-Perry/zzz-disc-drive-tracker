from .models import Disc
from django import forms

class DiscForm(forms.ModelForm):
    class Meta:
        model = Disc
        fields = ['set', 'main_stat', 'stat_1', 'stat_2', 'stat_3', 'stat_4']