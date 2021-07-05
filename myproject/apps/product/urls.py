from django.urls import path

from .views import product_validator

urlpatterns = [
    path('', product_validator, name='product-validator'),
]