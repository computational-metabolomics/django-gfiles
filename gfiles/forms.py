from django import forms
from gfiles.models import GenericFile


class GFileForm(forms.ModelForm):
    class Meta:
        model = GenericFile
        fields = ['data_file']