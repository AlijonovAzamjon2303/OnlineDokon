from django.contrib import admin
from .models import Category, Product

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Category)
admin.site.register(Product, AdminProduct)