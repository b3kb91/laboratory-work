from django.shortcuts import redirect, render
from django.views.generic import View

from webapp.forms import OrderForm
from webapp.models import Basket
from webapp.models.order import OrderProduct


class OrderCreate(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            baskets = Basket.objects.all()
            for basket in baskets:
                OrderProduct.objects.create(order=order, product=basket.product, quantity=basket.quantity)
            baskets.delete()
            return redirect('main')
        baskets = Basket.objects.all()
        return render(request, 'products/basket.html', {'baskets': baskets, 'order_form': form})
