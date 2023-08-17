from django.shortcuts import render
from .models import Item
from .forms import CreateItemForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,get_object_or_404
# Create your views here.
@login_required
def AddItemView(request):
   form= CreateItemForm()
   return render(request,'item/createItem.html',{'form':form}) 
