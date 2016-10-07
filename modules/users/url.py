from django.conf.urls import url
from .views import index, userlogin, userlogout, profile, edit

urlpatterns = [
	url(r'^$', index),
	url(r'^login/$', userlogin, name="login"),
	url(r'^logout/$', userlogout, name="logout"),
	url(r'^profile/$', profile, name="profile"),
	url(r'^profile/edit$', edit, name="edit")
]