from django import forms

# Create your forms here.
from .models import Product
import os

class ProductForm(forms.ModelForm, forms.Form):
    '''title       = forms.CharField(
                        widget=forms.TextInput(attrs={"placeholder": "Your Title",})
                        )
    email       = forms.EmailField()
    description = forms.CharField(
                        required=False, 
                        widget=forms.TextInput(
                            attrs={
                                "placeholder": "Your Description",
                                "rows": 20,
                                "cols": 60,
                                }
                            )
                        )
    price       = forms.DecimalField(decimal_places=2, max_digits=8)'''
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    
#    def clean_email(self, *args, **kwargs):
        '''email = self.cleaned_data.get("email")
        if not email == os.getenv("EMAIL"):
            raise forms.ValidationError('invalid email')
        return email'''


class RawProductForm(forms.Form):
    title       = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Title",}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.TextInput(
                            attrs={
                                "placeholder": "Your Description",
                                "rows": 20,
                                "cols": 60,
                                }
                            )
                        )
    price       = forms.DecimalField(decimal_places=2, max_digits=8)