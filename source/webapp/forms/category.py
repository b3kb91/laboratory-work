from django import forms
from webapp.models import Category
from django.forms import widgets


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'description']
        error_messages = {
            "title": {
                "required": "Поле обязательное"
            }
        }
        widgets = {
            'description': widgets.Textarea(attrs={'cols': 20, "rows": 5})}
