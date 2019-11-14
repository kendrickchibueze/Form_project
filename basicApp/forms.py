from django import forms
from django.core import validators

class formName(forms.Form):
    name = forms.CharField()
    email=forms.EmailField()
    verify_Email=forms.EmailField(label='please enter the same email again : ')
    text = forms.CharField(widget=forms.Textarea)
    # setting up a hidden field in the form
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_Email']
        if email !=vmail:
            raise forms.ValidationError('MAKE SURE EMAILS MATCH!')



