from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField()
    title = forms.CharField(widget=forms.TextInput())
    content = forms.CharField(widget=forms.Textarea)
