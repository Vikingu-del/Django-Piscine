from django import forms


class MovieForm(forms.Form):
    titles = forms.ChoiceField(
        label="movies",
        label_suffix="",
        choices=[],
        widget=forms.Select(attrs={"class": "form-input"}),
    )

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("choices", [])
        super().__init__(*args, **kwargs)
        self.fields["titles"].choices = choices
