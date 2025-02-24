from django.contrib import admin

# Register your models here.
# relative import
from .models import Product

admin.site.register(Product)

