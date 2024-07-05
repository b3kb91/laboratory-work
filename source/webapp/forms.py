from django import forms
from webapp.models import Product
from django.core.exceptions import ValidationError
from django.forms import widgets


class ProductForm(forms.ModelForm):
    remains = forms.IntegerField(min_value=0, label='Остаток')

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
