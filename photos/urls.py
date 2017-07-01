from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.hello, name='photos'),
	url(r'(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	url(r'upload', views.upload, name='upload'),
]