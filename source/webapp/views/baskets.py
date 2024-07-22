from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.db.models import Sum, F

from webapp.models import Product, Basket


class BasketAdd(View):

    def dispatch(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.product.remains > 0:
            basket, create = Basket.objects.get_or_create(product=self.product)
            if not create:
                if basket.quantity < self.product.remains:
                    basket.quantity += 1
            else:
                basket.quantity = 1
            basket.save()
        return redirect('main')


class BasketView(View):

    def get(self, request, *args, **kwargs):
        baskets = Basket.objects.all()
        total = baskets.aggregate(total_sum=Sum(F('quantity') * F('product__price')))['total_sum']
        return render(request, 'products/basket.html', {'baskets': baskets, 'total': total})


class BasketDelete(View):

    def dispatch(self, request, *args, **kwargs):
        self.basket = get_object_or_404(Basket, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.basket.quantity > 1:
            self.basket.quantity -= 1
            self.basket.save()
        elif self.basket.quantity == 1:
            self.basket.delete()
        return redirect('basket')

        # старое удаление
        # self.basket.delete()
        # return redirect('basket')
