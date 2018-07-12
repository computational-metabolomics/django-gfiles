import django_filters
from .models import GenericFile


class GFileFilter(django_filters.FilterSet):
    username = django_filters.CharFilter('user__username', lookup_expr='contains', label="Username")
    original_filename = django_filters.CharFilter('original_filename', lookup_expr='contains', label="Filename")

    class Meta:
        model = GenericFile
        fields = ('original_filename', 'username')
