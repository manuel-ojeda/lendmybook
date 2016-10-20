from django.conf.urls import url
from .views import index, userlogin, userlogout, profile, edit, view

urlpatterns = [
	url(r'^$', index),
	url(r'^login/$', userlogin, name="login"),
	url(r'^edit/$', edit, name="edit"),
	url(r'^logout/$', userlogout, name="logout"),
	url(r'^profile/$', profile, name="profile"),
	url(r'^(?P<id>\d+)', view, name="view"),
]