from django.shortcuts import render,redirect
from .models import Item
from .forms import CreateItemForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,get_object_or_404
# Create your views here.
@login_required
def AddItemView(request):
   
   if request.method=='POST':
      form= CreateItemForm(request.POST, request.FILES)
      if form.is_valid():
         #add item to database
         item=form.save(commit=False)
         item.created_by=request.user
         item.save()
         return redirect('item:detail',pk=item.id)
         
      return render(request,'item/createItem.html',
                 {'form':form}) 
         
   else:
      form= CreateItemForm()
      #get 
      return render(request,'item/createItem.html',
                 {'form':form}) 
