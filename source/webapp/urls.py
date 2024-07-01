from django.urls import path

from webapp.views import index, category_add_view, product_add_view, product_view, delete, product_edit_view


urlpatterns = [
    path('', index, name='products_view'),
    path('products/', index, name='products_view'),
    path('products/<int:pk>/', product_view, name="product_view"),
    path('categories/add', category_add_view, name='category_add_view'),
    path('products/add', product_add_view, name="product_add_view"),
    path('delete/<int:pk>/', delete, name="delete"),
    path('products/<int:pk>/edit', product_edit_view, name="product_edit_view"),
]
