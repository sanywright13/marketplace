from django.contrib import admin
from django.urls import path ,include
from .models import Item
from core.views import detailPage
app_name='item'
urlpatterns = [
  path('items/<int:pk>/',detailPage,name="detail")
]
