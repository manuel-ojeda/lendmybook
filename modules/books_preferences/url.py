from django.conf.urls import url
from .views import BookPreferencesDetail, NewBookPreferences

urlpatterns = [
	
	#url(r'^userbookpreferences/$', UserBookPreferences, name="userbookpreferences"),
	

	url(r'^book/(?P<pk>[0-9]+)$', BookPreferencesDetail.as_view()),
	url(r'^new/$',NewBookPreferences.as_view())
]