from django.conf.urls import url
from .views import postNewBaseBook, ShowBaseBook, ListAllBaseBooks, BaseBookImage

urlpatterns = [
	
	url(r'^postnewbasebook/$', postNewBaseBook, name="postnewbasebook"),
	
	url(r'^(?P<pk>[0-9]+)/$', ShowBaseBook.as_view()),
	url(r'^showallbasebooks/$', ListAllBaseBooks.as_view()),
	url(r'^basebookimage/(?P<pk>[0-9]+)$', BaseBookImage.as_view()),

]