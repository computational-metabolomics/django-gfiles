from django.conf.urls import url
from gfiles import views
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'gfiles/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/$', CreateView.as_view(
        template_name='gfiles/register.html',
        form_class=UserCreationForm,
        success_url='/'
    ), name='register'),
    url(r'^upload_gfile/$', views.GFileCreateView.as_view(), name='upload_gfile'),
    url(r'^gfile_summary/$', views.GFileListView.as_view(), name='gfile_summary'),
    url(r'^update/$', views.status_update, name='status_update'),
]

