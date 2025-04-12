from django.contrib import admin
from .models import Category, FoodItem, Order

admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(Order)
