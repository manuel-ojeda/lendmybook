from django.conf.urls import url
from .views import postNewBook, profile

urlpatterns = [

	url(r'^postnew/$', postNewBook, name="postnew"),
	url(r'^profile/$', profile, name="profile"),
]