from django.contrib import admin

from webapp.models import Category, Product, Order

admin.site.register(Category)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'created_at']
    sortable_by = ['-created_at']
    list_display_links = ["address"]
    search_fields = ['address', 'name']
    fields = ['id', 'name', 'created_at', 'phone']
    readonly_fields = ['created_at']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_at']
    list_filter = ['price', 'id']
    list_display_links = ["description"]
    search_fields = ['description', 'price']
    fields = ['description', 'price', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Product, ProductAdmin, Order, OrderAdmin)
