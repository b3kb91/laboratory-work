from django import forms
from webapp.models import Product
from django.core.exceptions import ValidationError

from django.forms import widgets


class ProductForm(forms.ModelForm):
    remains = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label="Цена")

    def clean_remains(self):
        remains = self.cleaned_data['remains']
        if remains < 0:
            raise ValidationError('Остаток не может быть ниже 0')
        else:
            return remains

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
            'created_at': widgets.DateInput(attrs={"type": "date"})}
