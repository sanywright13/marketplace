from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    class Meta:
        ordering=('name',)
        verbose_name_plural='categories'
    def __str__(self):
        return self.name    
    
class Item(models.Model):
    #if we delete a category all its items will be deleted
    Category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    descreption=models.TextField(blank=True,null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='items_images',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('name',)
    def __str__(self):
        return self.name