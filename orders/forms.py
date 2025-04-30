from django import forms

class OrderItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')
