from django.contrib import admin
from django.urls import path ,include
from .views import Index,Contact,detailPage
from django.conf.urls.static import static
from django.conf import settings
app_name='core'
urlpatterns = [
path('',Index,name='index'),
path('contact/',Contact,name='contact'),
#path('<int :pk>/',detailPage,name='item-detail')
]
# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()