#home/forms.py
from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
    #Extra validation example
    def clean_message(self):
        message=self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long")
        return message