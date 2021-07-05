from django.contrib import admin
from myproject.apps.product.models import ProductUnique

# Register your models here.
@admin.register(ProductUnique)
class ProductUniqueAdmin(admin.ModelAdmin):
    pass
