from django.conf.urls import url
from .views import postNewBookUser, profile, ShowBook, ListAllBooks
#ShowBook, ListAllBooks

urlpatterns = [

	url(r'^postnewuserbook/$', postNewBookUser, name="postnewuserbook"),
	url(r'^userbooks/$', profile, name="userbooks"),
	url(r'^(?P<pk>[0-9]+)/$', ShowBook.as_view()),
	url(r'^showallbasebooks/$', ListAllBooks.as_view()),
]

	#url(r'^(?P<pk>[0-9]+)/$', ShowBook.as_view()),
	#url(r'^showallbooks$', ListAllBooks.as_view()),
	#url(r'^getnew/$', getNewBook, name="getnew"),