from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from .views import home

from api.resources import NoteResource
note_resource = NoteResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(note_resource.urls)),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^$', home, name='home'),
]
