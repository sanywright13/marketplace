from django.contrib import admin
from django.urls import path ,include
from .views import Index
from django.conf.urls.static import static
app_name='dashbord'
urlpatterns = [
path('dashbord/',Index,name='index')

]
