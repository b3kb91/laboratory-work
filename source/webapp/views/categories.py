from django.views.generic import CreateView

from webapp.forms import CategoryForm


class CategoryCreateView(CreateView):
    template_name = 'category/create_category.html'
    form_class = CategoryForm
