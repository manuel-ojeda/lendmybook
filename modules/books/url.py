from django.conf.urls import url
from .views import postNewBookUser, profile

urlpatterns = [

	url(r'^postnewuserbook/$', postNewBookUser, name="postnew"),
	url(r'^profile/$', profile, name="profile"),
	#url(r'^getnew/$', getNewBook, name="getnew"),
]