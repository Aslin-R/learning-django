from django.db import models

class MenuCategory(models.Model):
    menu_category_name=models.CharField(max_length=200)

class Menu(models.Model):
    menu_itm=models.CharField(max_length=100)
    price=models.IntegerField(null=False)
    category_id=models.ForeignKey(MenuCategory,on_delete=models.PROTECT,default=None,related_name='category_name')

class  DrinksCategory(models.Model):
    category_name=models.CharField(max_length=200)

class Drinks(models.Model):
    drink=models.CharField(max_length=200)
    price=models.IntegerField()
    category_id=models.ForeignKey(DrinksCategory,on_delete=models.PROTECT,default=None)

class Customer(models.Model):
    name=models.CharField(max_length=100)
    reservation_day=models.CharField(max_length=100)
    seats=models.IntegerField()

    def __str__(self):
        return self.name

class Logger(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    time_log=models.TimeField(help_text='Enter the current time')

class Booking(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    guest_count=models.IntegerField()
    reservation_time=models.DateField(auto_now=True)
    comments=models.CharField(max_length=1000)
    


