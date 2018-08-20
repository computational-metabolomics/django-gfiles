import django_filters
from .models import GenericFile


class GFileFilter(django_filters.FilterSet):
    """ Class for filtering Generic Files using django_filters.FilterSet

    Filters available for the username of the user who uploaded the file and the original filename (the original name
    can be different to the name of the file that is stored if multiple files of the same name are uploaded at the same
    time)
    """
    username = django_filters.CharFilter('user__username', lookup_expr='contains', label="Username")
    original_filename = django_filters.CharFilter('original_filename', lookup_expr='contains', label="Filename")

    class Meta:
        model = GenericFile
        fields = ('original_filename', 'username')


class TrackTasksFilter(django_filters.FilterSet):
    """ Class for filtering Tracked tasks
    """
    username = django_filters.CharFilter('user__username', lookup_expr='contains', label="Username")
    track_id = django_filters.CharFilter('track_id', lookup_expr='contains', label="Username")
    status = django_filters.CharFilter('status', lookup_expr='contains', label="status")

    class Meta:
        model = GenericFile
        fields = ('username', 'track_id', 'status')
