from django.contrib import admin
from .models import Menu
from .models import MenuCategory
from .models import DrinksCategory
from .models import Drinks

from .models import Booking
from .models import Employees

# Register your models here.

admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(DrinksCategory)
admin.site.register(Drinks)

admin.site.register(Employees)
@admin.register(Booking) 

class PersonAdmin(admin.ModelAdmin): 
    list_display = ("last_name", "first_name") 
    search_fields = ("first_name__startswith", ) 

