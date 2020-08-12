from rest_framework import serializers
from .models import *
from menu.models import MenuItem
from accounts.models import RestaurantAccount, PersonelAccount
from accounts.serializers import PersonelAccountSerializer


class OrdersNewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'ordered_by', 'ordered_by_name',
                  'order_type', 'order_time', 'order_status')


class MenuItemDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'price', 'dprice', 'poster',)


class OrderItemsNewSerializers(serializers.ModelSerializer):
    order_item = MenuItemDetailsSerializer(many=False)

    class Meta:
        model = OrderItems
        fields = ('id', 'order_item', 'quantity')
        depth = 1


class OrdersIdSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id',)


class RestaurantNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAccount
        fields = ('id', 'name')


class OrdersSerializers(serializers.ModelSerializer):
    items = OrderItemsNewSerializers(
        many=True, source='Order_item_lists')
    ordered_from = RestaurantNameSerializer(many=False)
    ordered_by_name = PersonelAccountSerializer(many=False)

    class Meta:
        model = Orders
        fields = ('id', 'ordered_by', 'ordered_by_name', 'ordered_from',
                  'order_type', 'order_time', 'order_status', 'created_at', 'items')
