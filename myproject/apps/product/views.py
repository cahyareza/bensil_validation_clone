from django.shortcuts import render
from django.db.models import Q
from myproject.apps.product.models import ProductUnique
from myproject.apps.product.forms import ProductValidationForm

def product_validator(request):
    form = ProductValidationForm(request.GET or None)
    products = None
    unique = False
    if request.GET.get('unique'):
        products = ProductUnique.objects.all()
        unique = products.filter(Q(unique__icontains=request.GET.get('unique')))
    context = {
        "products": products,
        "unique": unique,
        "form": form,
    }

    return render(request, 'index.html', context)
