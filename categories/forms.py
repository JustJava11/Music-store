from django import forms
from categories.models import Category

class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=256)

    class Meta:
        model = Category
        fields = ['title', 'image']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': "Category",
                    'class': 'form-control',
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
