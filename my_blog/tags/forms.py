from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from .models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
        labels = {
            'name': 'Name',
            'slug': 'Slug'
        }

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'contact'
        self.helper.layout = Layout(
            Fieldset(

            )
            ,
            ButtonHolder(
                Submit('submit', 'Add', css_class='btn btn-primary'),
                css_class="d-flex justify-content-end"
            )
        )
