from django.conf.urls import url
from .views import index, user

urlpatterns = [
	url(r'^$', index, name="index"),
	url(r'user/^$', user, name="user"),
]