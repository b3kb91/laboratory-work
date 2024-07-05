from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm
from webapp.models import Product, Category


def index(request):
    products = Product.objects.order_by('-created_at')
    return render(request, 'products_view.html', context={"products": products})


def product_add_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "product_add_view.html", context={"categories": categories})
    else:
        description = request.POST.get("description")
        if description == '':
            description = None

        product = Product.objects.create(
            title=request.POST.get("title"),
            price=request.POST.get("price"),
            image=request.POST.get("image"),
            category=request.POST.get("category"),
            description=description,
            category_id=request.POST.get("category_id"),
        )
        return redirect("product_view", pk=product.pk)


def delete(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect("products_view")


def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_view", pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, "product_edit_view.html", {"form": form})


def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_view.html", context={"product": product})


def category_add_view(request):
    if request.method == "GET":
        return render(request, "category_add_view.html")
    else:
        description = request.POST.get("description")
        if description == '':
            description = None

        category = Category.objects.create(
            title=request.POST.get("title"),
            description=description
        )
        return redirect("products_view")
