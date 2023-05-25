from django.shortcuts import render
from myproject.apps.product.models import ProductUnique
from myproject.apps.product.forms import ProductValidationForm

def product_validator(request):
    form = ProductValidationForm(request.GET or None)
    products = None
    unique = False
    if request.GET.get('unique'):
        products = ProductUnique.objects.all()
        try:
            unique = products.get(unique=request.GET.get('unique'))
        except:
            unique = False
    context = {
        "products": products,
        "unique": unique,
        "form": form,
    }

    return render(request, 'index.html', context)
