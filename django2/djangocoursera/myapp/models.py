from django.db import models

class MenuCategory(models.Model):
    menu_category_name=models.CharField(max_length=200)

class Menu(models.Model):
    menu_itm=models.CharField(max_length=100)
    price=models.IntegerField(null=False)
    category_id=models.ForeignKey(MenuCategory,on_delete=models.PROTECT,default=None,related_name='category_name')