from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)


    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category,related_name="items",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255,blank=True,null=True)
    price = models.IntegerField()
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Chon anh",blank=True,null=True)
    created_by = models.ForeignKey(User,related_name="items",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)


    def __str__(self) -> str:
        return self.name
