from django import forms
from webapp.models import Product
from django.forms import widgets


class ProductForm(forms.ModelForm):
    remains = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label="Цена")

    class Meta:
        model = Product
        fields = ['title', 'price', 'image', 'category', 'description', 'remains']
        error_messages = {
            "image": {
                "required": "Поле обязательное"
            },
            "title": {
                "required": "Поле обязательное"
            }
        }
        widgets = {
            'description': widgets.Textarea(attrs={'cols': 20, "rows": 5}),
            'created_at': widgets.DateInput(attrs={"type": "date"}),
        }


class SearchProduct(forms.Form):
    title = forms.CharField(label='Поиск товара', max_length=200, required=False)
