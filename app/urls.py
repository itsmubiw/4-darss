from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView, DishListCreateView, DishDetailView, ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('dishes/', DishListCreateView.as_view(), name='dish-list'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
