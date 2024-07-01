from django import forms
from webapp.models import Product, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'image', 'category', 'description']
