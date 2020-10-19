from django.contrib import admin

from .models import Shoe, Phone, Laptop, Business, Customer


admin.site.register(Shoe)
admin.site.register(Phone)
admin.site.register(Laptop)
admin.site.register(Business)
admin.site.register(Customer)
