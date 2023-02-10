from django.db import models

class MenuCategory(models.Model):
    menu_category_name=models.CharField(max_length=200)

class Menu(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    
    def __str__(self):
        return self.name

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


class Booking(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    guest_count=models.IntegerField()
    reservation_time=models.DateField(auto_now=True)
    comments=models.CharField(max_length=1000)
    
    def __str__(self): 
        return f"{self.last_name}, {self.first_name}" 

class Employees(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    role=models.CharField(max_length=100)
    shift=models.IntegerField()

    def __str__(self) -> str:
        return self.first_name

