from django.urls import path

from webapp.views import ProductListView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductUpdateView
from webapp.views import CategoryCreateView, BasketAdd, BasketView, BasketDelete

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('products/', ProductListView.as_view(), name='main'),
    path('products/<int:pk>/detail/', ProductDetailView.as_view(), name="detail"),
    path('categories/add', CategoryCreateView.as_view(), name='create_category'),
    path('products/add', ProductCreateView.as_view(), name="create"),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name="delete"),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name="update"),
    path('basket/<int:pk>/', BasketAdd.as_view(), name="basket_add"),
    path('basket/', BasketView.as_view(), name="basket"),
    path('basket/<int:pk>/delete/', BasketDelete.as_view(), name="basket_delete"),
]
