from django.conf.urls import url, include
from gfiles import views
# from django.contrib.auth import views as auth_views




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^upload_gfile/$', views.GFileCreateView.as_view(), name='upload_gfile'),
    url(r'^gfile_summary/$', views.GFileListView.as_view(), name='gfile_summary'),
    url(r'^update/$', views.status_update, name='status_update'),
    url(r'^success/$', views.success, name='success'),
    url(r'^track_tasks/$', views.TrackTasksListView.as_view(), name='track_tasks'),
    url(r'^delete_track_task/(?P<pk>[\w]+)/$', views.TrackTasksDeleteView.as_view(), name='delete_track_task'),
    url(r'^track_task_progress/(?P<pk>\d+)/$', views.TrackTasksProgressView.as_view(), name='track_task_progress')
]

