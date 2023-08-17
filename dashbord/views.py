from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from item.models import Item
# Create your views here.
app_name='dashbord'
@login_required
def Index(request):
    items=Item.objects.filter(created_by=request.user)
    return render(request,'dashboard/index.html',{'items':items})
    
