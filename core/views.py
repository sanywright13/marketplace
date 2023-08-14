from django.shortcuts import render
from item.models import Item , Category

# Create your views here.
def Index(request):
    items=Item.objects.filter(is_sold=False)[:1]
    categories=Category.objects.all()
    context={
        'items':items,
        'categories':categories
    }
    return render(request,'core/index.html',context)


def Contact(request):
    return render(request,'core/contact.html')