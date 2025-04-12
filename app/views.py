from rest_framework import generics
from .models import Category, FoodItem, Order
from .serializers import CategorySerializer, FoodItemSerializer, OrderSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class FoodItemListCreateView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsAdminOrReadOnly]

class FoodItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsAdminOrReadOnly]

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrAdmin]


from .throttling import CategoryThrottle, DishThrottle, ReviewThrottle

class CategoryListCreateView(generics.ListCreateAPIView):
    ...
    throttle_classes = [CategoryThrottle]

class DishListCreateView(generics.ListCreateAPIView):
    ...
    throttle_classes = [DishThrottle]

class ReviewListCreateView(generics.ListCreateAPIView):
    ...
    throttle_classes = [ReviewThrottle]
