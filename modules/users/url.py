from django.conf.urls import url
from .views.FrontUser import *
from .views.ApiUser import *

urlpatterns = [
	url(r'^$', index),
	url(r'^login/$', userlogin, name="login"),
	url(r'^logout/$', userlogout, name="logout"),
	url(r'^profile/$', profile, name="profile"),
	url(r'^profile/edit$', edit, name="edit"),

	url(r'^login/first-time$', SignUp, name="signUpApi"),
	url(r'^login/$', SignIn, name="signInApi"),
]