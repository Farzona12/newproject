from django.db import models
from django.contrib.auth.models import AbstractUser

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


class User(AbstractUser):
    pass

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.qty} x {self.product.name}"
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)