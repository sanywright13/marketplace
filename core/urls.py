from django.contrib import admin
from django.urls import path ,include
from .views import Index,Contact
app_name='core'
urlpatterns = [
path('',Index,name='index'),
path('contact/',Contact,name='contact')
]
