from django.conf.urls import url
from .views import postNewBookUser, profile, search, view, list
#ShowBook, ListAllBooks

urlpatterns = [
	url(r'^postnewuserbook/$', postNewBookUser, name="postnewuserbook"),
	url(r'^userbooks/$', profile, name="userbooks"),
	url(r'^search/$', search, name="search"),
	url(r'^list/([0-9]+)', list, name="list"),
]

	#url(r'^(?P<pk>[0-9]+)/$', ShowBook.as_view()),
	#url(r'^showallbooks$', ListAllBooks.as_view()),
	#url(r'^getnew/$', getNewBook, name="getnew"),