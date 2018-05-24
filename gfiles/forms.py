from django import forms
from gfiles.models import GenericFile
import os

class GFileForm(forms.ModelForm):
    class Meta:
        model = GenericFile
        fields = ['data_file']

    # class Media:    # only required if using the django-filer app
    #     extend = False
    #     css = {
    #         'all': [
    #             'filer/css/admin_filer.css',
    #         ]
    #     }
    #     js = (
    #         'admin/js/core.js',
    #         'admin/js/jquery.js',
    #         'admin/js/jquery.init.js',
    #         'admin/js/admin/RelatedObjectLookups.js',
    #         'admin/js/actions.js',
    #         'admin/js/urlify.js',
    #         'admin/js/prepopulate.js',
    #         'filer/js/libs/dropzone.min.js',
    #         'filer/js/addons/dropzone.init.js',
    #         'filer/js/addons/popup_handling.js',
    #         'filer/js/addons/widget.js',
    #         'admin/js/related-widget-wrapper.js',
    #     )

