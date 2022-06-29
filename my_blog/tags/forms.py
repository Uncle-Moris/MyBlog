from .models import Tag
from django import forms



class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
