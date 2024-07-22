from django import forms
from webapp.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'address', 'phone']
        error_messages = {
            "name": {
                "required": "Поле обязательное"
            },
            "address": {
                "required": "Поле обязательное"
            },
            "phone": {
                "required": "Поле обязательное"
            }

        }
