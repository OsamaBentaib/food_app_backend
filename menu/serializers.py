from rest_framework import serializers
from .models import *
from accounts.models import ServiceOffer, RestaurantAccount
from accounts.serializers import RestaurantAccountSerializer, VerificationSerializer, ServiceOfferAddSerializer

# class IngredientsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ingredients
#         fields = ['id', 'Item', 'title', 'poster', 'created_at']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id',
                  'rst_id',
                  'title',
                  'description',
                  'price',
                  'dprice',
                  'categories',
                  'poster',
                  'created_at')

# class MenuItemDetailsSerializer(serializers.ModelSerializer):
#     ServiceOffer = ServiceOfferSerializer(
#         many=False, source='serviceOfferType')
#     Ingredients = IngredientsSerializer(
#         many=True, source='Ingredients_item')

#     class Meta:
#         model = MenuItem
#         fields = ('id',
#                   'rst_id',
#                   'title',
#                   'description',
#                   'price',
#                   'dprice',
#                   'poster',
#                   'created_at',
#                   'ServiceOffer',
#                   'Ingredients')


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id', 'Item', 'title', 'poster']


class MenuItemDetailsSerializer(serializers.ModelSerializer):
    rst_id = RestaurantAccountSerializer(many=False)
    class Meta:
        model = MenuItem
        fields = ('id',
                  'rst_id',
                  'title',
                  'description',
                  'price',
                  'dprice',
                  'poster',
                  'created_at',
                  )
        depth = 1
