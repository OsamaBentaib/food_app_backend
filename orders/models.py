from django.db import models
from django.conf import settings
from accounts.models import PersonelAccount, RestaurantAccount
from menu.models import MenuItem
# Create your models here.
STATUS_CHOICES = (
    ('CREATED', 'CREATED'),
    ('SUBMITED', 'SUBMITED'),
    ('CONFIRMED', 'CONFIRMED'),
    ('READY', 'READY'),
    ('DELEVERED', 'DELEVERED'),
    ('CANCLED', 'CANCLED'),
    ('FINISHED', 'FINISHED'),
)
ORDERS_TYPE_CHOICES = (
    ('DELIVERY', 'DELIVERY'),
    ('TAKEAWAY', 'TAKEAWAY'),
    ('DININ', 'DININ'),
)


class Orders(models.Model):
    ordered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered_by_name = models.ForeignKey(
        PersonelAccount, on_delete=models.CASCADE)
    ordered_from = models.ForeignKey(
        RestaurantAccount, on_delete=models.CASCADE)
    order_type = models.CharField(choices=ORDERS_TYPE_CHOICES, max_length=100)
    order_time = models.CharField(max_length=50)
    order_status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItems(models.Model):
    order = models.ForeignKey(
        Orders, related_name='Order_item_lists', on_delete=models.SET_NULL, null=True)
    order_item = models.ForeignKey(
        MenuItem, related_name='Order_item_to_lists', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
