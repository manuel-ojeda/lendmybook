from django.conf.urls import url
from .views import EventDetail, NewEvent

urlpatterns = [
	
	#url(r'^userbookpreferences/$', UserBookPreferences, name="userbookpreferences"),
	

	url(r'^(?P<pk>[0-9]+)$', EventDetail.as_view()),
	url(r'^new/$',NewEvent.as_view())
]