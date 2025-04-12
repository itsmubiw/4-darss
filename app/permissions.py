from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Kategoriya nomi")
    description = models.TextField(blank=True, null=True, verbose_name="Tavsif")

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=255, verbose_name="Taom nomi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="foods", verbose_name="Kategoriya")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narx")
    description = models.TextField(blank=True, null=True, verbose_name="Tavsif")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", verbose_name="Foydalanuvchi")
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="orders", verbose_name="Taom")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Miqdori")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, verbose_name="Jami narx")
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Kutilmoqda'), ('completed', 'Tamomlandi'), ('canceled', 'Bekor qilindi')],
        default='pending',
        verbose_name="Holat"
    )
    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name="Buyurtma berilgan sana")

    def save(self, *args, **kwargs):
        self.total_price = self.food_item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Buyurtma {self.id} - {self.user.username}"
