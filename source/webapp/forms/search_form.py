from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label='Поиск товара', max_length=200, required=False)
