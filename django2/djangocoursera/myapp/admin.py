from django.contrib import admin
from .models import Menu
from .models import MenuCategory
from .models import DrinksCategory
from .models import Drinks
from .models import Logger
from .models import Booking
# Register your models here.


admin.site.register(Menu)
admin.site.register(MenuCategory)

admin.site.register(DrinksCategory)
admin.site.register(Drinks)

admin.site.register(Logger)

admin.site.register(Booking)