from django import forms
from myproject.apps.product.models import ProductUnique

class ProductValidationForm(forms.ModelForm):
    unique = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Masukan kode unik',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )
    class Meta:
        model = ProductUnique
        fields = ["unique"]

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(ProductValidationForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['unique'].required = True

        # 2. Help text
        self.fields['unique'].help_text = '*Masukan kode unik produk yang tertera dibawah QR Code'