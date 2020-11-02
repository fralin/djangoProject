from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SiteForm(forms.ModelForm):
    class Meta:
        model = models.Site
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))