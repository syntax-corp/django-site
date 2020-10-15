from django import forms

# Create your forms here.
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField(required=False)
    price       = forms.DecimalField(decimal_places=2, max_digits=8)