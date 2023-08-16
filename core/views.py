from django.shortcuts import render, redirect,get_object_or_404
from item.models import Item , Category
from django.contrib.auth import login
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
# Create your views here.
def Index(request):
    items=Item.objects.filter(is_sold=False)[:8]
    categories=Category.objects.all()
    context={
        'items':items,
        'categories':categories
    }
    return render(request,'core/index.html',context)

def SignUpView(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            print('validddd')
            user=form.save()
            #login(request,user)
            return redirect('core:login')
        messages.error(request, "Unsuccessful registration. Invalid information.")
        return render(request,'core/signup.html',
                      {'form':form})
    else:
        form=SignUpForm()
        return render(request,'core/signup.html',
                      {'form':form})
def LogInView(request):
    if request.method=='POST':
        form =LoginForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password') 
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('core:index')
            messages.error(request,"Invalid username or password.")
        messages.error(request,"Invalid username or password.")
        return render(request,'core/login.html',{'form':form})
    else:
        form=AuthenticationForm()
        return render(request,'core/login.html',{'form':form}) 
            
        
            
    
    pass
    
def Contact(request):
    return render(request,'core/contact.html')
@login_required
def detailPage(request,pk):
    item=get_object_or_404(Item,pk=pk)
    itemCat=item.Category.name
    related_items=Item.objects.filter(Category__name=itemCat,is_sold=False).exclude(pk=pk)[:3]
    return render(request,'core/detail.html',{'item':item,'related_items':related_items})
    