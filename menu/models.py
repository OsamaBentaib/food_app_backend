from django.db import models
from django.conf import settings
from django.utils import timezone
from accounts.models import RestaurantAccount


class MenuItem(models.Model):
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rst_id = models.ForeignKey(RestaurantAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dprice = models.DecimalField(max_digits=5, decimal_places=2)
    categories = models.CharField(max_length=500)
    poster = models.ImageField(
        upload_to='menu', max_length=90000, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ingredients(models.Model):
    Item = models.ForeignKey(MenuItem, related_name='makers', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    poster = models.ImageField(
        upload_to='menu/ingredients', max_length=90000, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            unique_together = ['Item', 'id']
            ordering = ['id']

    def __str__(self):
        return self.title