from django.contrib import admin

from webapp.models import Category, Product

admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_at']
    list_filter = ['price', 'id']
    list_display_links = ["description"]
    search_fields = ['description', 'price']
    fields = ['description', 'price', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Product, ProductAdmin)
