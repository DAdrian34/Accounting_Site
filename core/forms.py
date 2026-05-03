# core/forms.py

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nume',
        widget=forms.TextInput(attrs={'placeholder': 'Numele tău'}),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
    )
    message = forms.CharField(
        label='Mesaj',
        widget=forms.Textarea(attrs={'placeholder': 'Scrie mesajul tău aici'}),
    )
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'tabindex': '-1',
            'class': 'honeypot-field',
        }),
    )

    def clean_website(self):
        website = self.cleaned_data.get('website')

        if website:
            raise forms.ValidationError('Invalid submission.')

        return website