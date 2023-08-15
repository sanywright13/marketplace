from django.shortcuts import render,get_object_or_404
from item.models import Item , Category
from .forms import SignUpForm
# Create your views here.
def Index(request):
    items=Item.objects.filter(is_sold=False)[:4]
    categories=Category.objects.all()
    context={
        'items':items,
        'categories':categories
    }
    return render(request,'core/index.html',context)

def SignUpView(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('core:login')
    else:
        form=SignUpForm()
        return render(request,'core/signup.html',
                      {'form':form})
def Contact(request):
    return render(request,'core/contact.html')

def detailPage(request,pk):
    item=get_object_or_404(Item,pk=pk)
    itemCat=item.Category.name
    related_items=Item.objects.filter(Category__name=itemCat,is_sold=False).exclude(pk=pk)[:3]
    return render(request,'core/detail.html',{'item':item,'related_items':related_items})
    