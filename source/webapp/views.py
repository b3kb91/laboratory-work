from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm
from webapp.models import Product, Category


def index(request):
    products = Product.objects.order_by('-created_at')
    return render(request, 'products_view.html', context={"products": products})


def product_add_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "product_add_view.html", context={"form": form})
    else:
        description = request.POST.get("description")
        if description == '':
            description = None

        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.description = description
            return redirect("product_view", pk=product.pk)

        return render(
            request,
            "product_add_view.html",
            context={"form": form}
        )


def delete(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, "products_delete.html", context={"product": product})
    else:
        product.delete()
        return redirect("products_view")


def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(
            request,
            "product_edit_view.html",
            context={"form": form}
        )
    else:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_view", pk=product.pk)
        return render(
            request,
            "product_edit_view.html",
            {"form": form}
        )


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
