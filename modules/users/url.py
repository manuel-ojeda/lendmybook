from django.conf.urls import url
from .views import profile, edit, userlogin, userlogout
from .views import SignUp, LogIn

urlpatterns = [
	url(r'^login/$', userlogin, name="login"),
	url(r'^logout/$', userlogout, name="logout"),
	url(r'^profile/$', profile, name="profile"),
	url(r'^profile/edit$', edit, name="edit"),

	url(r'^login/sign$', SignUp.as_view()),
	url(r'^login/$', LogIn.as_view()),
]