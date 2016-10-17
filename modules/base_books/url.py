from django.conf.urls import url
from .views import postNewBaseBook

urlpatterns = [
	
	url(r'^postnewbasebook/$', postNewBaseBook, name="postnewbasebook"),
]