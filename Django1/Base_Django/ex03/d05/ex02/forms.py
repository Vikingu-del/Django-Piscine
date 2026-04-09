from django import forms


class Ex02Form(forms.Form):
    user_text = forms.CharField(
        label='Enter some text',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Type something here...',
            'class': 'form-input'
        })
    )