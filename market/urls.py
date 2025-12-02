from django.urls import path
from .views import *

urlpatterns = [
    path("market_create/", MarketCreateView.as_view(), name="create_market"),
    path("market_list/", MarketListView.as_view(), name="market_list"),
    path("market_detail/<int:pk>", MarketDetailView.as_view(), name="market_detail"),
    path("market_update/<int:pk>", MarketUpdateView.as_view(), name="update_market"),
    path("market_delete_confirm/<int:pk>", MarketDeleteView.as_view(), name="market_delete_confirm"),
]
