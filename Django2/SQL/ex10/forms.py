from django import forms
from .models import People

class SearchForm(forms.Form):
    min_release_date = forms.DateField(label='Movies minimum release date (format yyyy-mm-dd)')
    max_release_date = forms.DateField(label='Movies maximum release date (format yyyy-mm-dd)')
    min_diameter = forms.IntegerField(label='Planet diameter greater then')

    gender =  forms.ChoiceField(
        label='Character gender',
        choices=[],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genders = People.objects.values_list('gender', flat=True).distinct()
        self.fields['gender'].choices = [(g, g) for g in genders if g]