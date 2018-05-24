import django_filters
from .models import GenericFile


class GFileFilter(django_filters.FilterSet):

    class Meta:
        model = GenericFile
        fields = {
            'original_filename': ['contains']
        }
