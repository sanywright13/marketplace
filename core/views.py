from django.shortcuts import render,get_object_or_404
from item.models import Item , Category

# Create your views here.
def Index(request):
    items=Item.objects.filter(is_sold=False)[:4]
    categories=Category.objects.all()
    context={
        'items':items,
        'categories':categories
    }
    return render(request,'core/index.html',context)


def Contact(request):
    return render(request,'core/contact.html')

def detailPage(request,pk):
    item=get_object_or_404(Item,pk=pk)
    itemCat=item.Category.name
    related_items=Item.objects.filter(Category__name=itemCat,is_sold=False).exclude(pk=pk)[:3]
    return render(request,'core/detail.html',{'item':item,'related_items':related_items})
    