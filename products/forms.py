from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'description',
            'product_image',
            'category',
            'quantity',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'product_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        def clean_quantity(self):
            quantity = self.cleaned_data.get('quantity')
            if quantity < 0:
                raise forms.ValidationError("Quantity cannot be negative.")
            return quantity

        def clean_price(self):
            price = self.cleaned_data.get('price')
            if price <= 0:
                raise forms.ValidationError("Price must be greater than zero.")
            return price