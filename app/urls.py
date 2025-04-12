from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView, FoodItemListCreateView, FoodItemDetailView, OrderListCreateView, OrderDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('food-items/', FoodItemListCreateView.as_view(), name='fooditem-list'),
    path('food-items/<int:pk>/', FoodItemDetailView.as_view(), name='fooditem-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
