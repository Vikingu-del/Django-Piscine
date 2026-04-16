from django import forms

class MovieForm(forms.Form):
    titles = forms.ChoiceField(
        label='movies',
        label_suffix='',
        choices = [],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    opening_crawl = forms.CharField(
        label = 'Write something for the opening crawl',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
    )

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)
        self.fields['titles'].choices = choices
