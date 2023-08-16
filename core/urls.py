from django.contrib import admin
from django.urls import path ,include
from .views import Index,Contact,detailPage,SignUpView,LogInView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
app_name='core'
urlpatterns = [
path('',Index,name='index'),
path('signup/',SignUpView,name='signup'),
path('login/',LogInView,name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name='core/logout.html'),name='logout'),
path('contact/',Contact,name='contact'),

]
# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()