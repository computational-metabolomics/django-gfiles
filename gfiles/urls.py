from django.conf.urls import url
from gfiles import views


urlpatterns = [
    url('upload_gfile/', views.GFileCreateView.as_view(), name='upload_gfile'),
    url('gfile_summary/', views.GFileListView.as_view(), name='gfile_summary'),
    url(r'^update/$', views.status_update, name='status_update'),
]