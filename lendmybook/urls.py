from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('modules.landing.url', namespace="landing")),
    url(r'^books/', include('modules.books.url', namespace="books")),
    url(r'^basebooks/', include('modules.base_books.url', namespace="base_books")),
    

    url(r'^api/books/', include('modules.books.url', namespace="apibooks")),
    url(r'^api/basebooks/', include('modules.base_books.url', namespace="apibasebooks")),
    #url(r'^api/bookpreferences/', include('modules.books_preferences.url', namespace="apibookspreferences")),
    #url(r'^api/events/', include('modules.events.url', namespace="apievents")),
    url(r'^api/user/', include('modules.users.url', namespace="apiusers")),
    #url(r'^api/userpreferences/', include('modules.user_preferences.url', namespace="apiuserpreferences")),
    #url(r'^api-auth/', obtain_jwt_token),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



