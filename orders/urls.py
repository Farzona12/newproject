from django.urls import path
from .views import (
    OrderCreateView,
    OrderDetailView,
    AddToCartView,
    RemoveFromCartView,
    UpdateCartItemView,
    CartDetailView,
)
urlpatterns = [
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('cart/', CartDetailView.as_view(), name='cart_detail'),
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart/update/<int:product_id>/', UpdateCartItemView.as_view(), name='update_cart_item'),
]
