from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import Order, OrderItem, Product, User, Cart, CartItem



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



class OrderCreateView(View):
    
    def post(self, request):
        user = request.user
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)

        total_sum = sum(item.product.price * item.qty for item in cart_items)
        order = Order.objects.create(user=user, total_sum=total_sum)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                qty=item.qty,
                price=item.product.price
            )

        cart_items.delete()  

        return redirect('order_detail', order_id=order.id)
    
    def __str__(self):
        return f"OrderItem {self.id} of Order {self.order.id}"
    
class OrderDetailView(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id, user=request.user)
        order_items = OrderItem.objects.filter(order=order)
        return render(request, 'order_detail.html', {'order': order, 'order_items': order_items})
    
class CartView(View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})
    
class AddToCartView(View):
    def post(self, request, product_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.qty += 1
            cart_item.save()
        return redirect('cart')
    
class RemoveFromCartView(View):
    def post(self, request, item_id):
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        cart_item.delete()
        return redirect('cart')
    
class UpdateCartItemView(View):
    def post(self, request, item_id):
        qty = int(request.POST.get('qty', 1))
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        cart_item.qty = qty
        cart_item.save()
        return redirect('cart')
    
    def __str__(self):
        return f"CartItem {self.id} in Cart {self.cart.id}"
    

class CartDetailView(View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        return render(request, 'cart_detail.html', {'cart': cart, 'cart_items': cart_items})
    
class OrderListView(View):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        return render(request, 'order_list.html', {'orders': orders})
    
    def __str__(self):
        return f"Cart of {self.user.username}"
    
