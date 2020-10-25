from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^location/(\d)',views.open_location, name='open_details'),
    url(r'^location/location/(\d)',views.open_location, name='open_details'),
    url(r'^search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
