from django.conf.urls import url
from .views import BookPreferencesDetail

urlpatterns = [
	
	#url(r'^userbookpreferences/$', UserBookPreferences, name="userbookpreferences"),
	

	url(r'^bookpreferences/(?P<pk>[0-9]+)$', BookPreferencesDetail.as_view()),
]