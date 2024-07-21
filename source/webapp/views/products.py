from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from webapp.forms import SearchForm, ProductForm
from webapp.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products.html'
    ordering = ['category', 'title']
    paginate_by = 6

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(remains__gte=1)
        if self.search_value:
            queryset = queryset.filter(
                Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context


class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    template_name = 'products/product_update.html'
    model = Product
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    success_url = reverse_lazy('main')


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Product
