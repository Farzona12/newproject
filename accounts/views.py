from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# ✅ Человек 3 — Заказы (OrderCreate) + Админка
# Функционал:

# Модель Order + OrderItem

# Order: user, created_at, total_sum

# OrderItem: product, qty, price

# Создание заказа (CBV: OrderCreateView)

# берём товары из корзины

# создаём OrderItems

# очищаем корзину

# OrderDetailView

# пользователь видит свой заказ (без статусов)

# Cart + CartItem

# добавление товара

# удаление

# изменение количества
from django.views import View
from .models import Order, OrderItem, Cart, CartItem

class OrderCreateView(View):
    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        order = Order.objects.create(user=request.user, total_sum=0)
        total_sum = 0

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                qty=item.qty,
                price=item.product.price
            )
            total_sum += item.qty * item.product.price

        order.total_sum = total_sum
        order.save()

        cart.items.all().delete() 

        return redirect('order_detail', pk=order.pk)

class OrderDetailView(View):
    def get(self, request, pk):
        order = Order.objects.get(pk=pk, user=request.user)
        return render(request, 'order_detail.html', {'order': order})
    
class AddToCartView(View):
    def post(self, request, product_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
        cart_item.qty += 1
        cart_item.save()
        return redirect('cart_detail')
    
class RemoveFromCartView(View):
    def post(self, request, product_id):
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
        cart_item.delete()
        return redirect('cart_detail')

