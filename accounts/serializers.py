from rest_framework import serializers
from .models import *


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServicesChoices
        fields = ('id', 'service')


class TokenTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenType
        fields = ('id', 'user', 'account')


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('id', 'name')


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ('id', 'name', 'country')


class ServiceOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOffer
        fields = ('rst_id', 'isDelivery', 'isNcDelivery',
                  'isTakeaway', 'isDinIn', 'created_at', 'updated_at')


class ServiceOfferAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOffer
        fields = ("id", 'rst_id', 'isDelivery',
                  'isNcDelivery', 'isTakeaway', 'isDinIn')


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verifications
        fields = ("id", "rst_id", "isVirefied")


class RestaurantLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = RestaurantLocations
        fields = ('id', 'added_by', 'long', 'lat')


class RestaurantAccountSerializer(serializers.ModelSerializer):
    serviceOffer = ServiceOfferAddSerializer(
        many=False, source='serviceOfferType')
    location = RestaurantLocationSerializers(
        many=False, source="Restaurant_location")

    class Meta:
        model = RestaurantAccount
        fields = ('id', 'added_by', 'name', 'address', 'city', 'Service', 'Categorie',
                  'bio', 'website', 'avatar', 'phone', 'serviceOffer', 'isVirefied', 'status', 'location', 'created_at', 'updated_at')


class RestaurantAccountAddSerializer(serializers.ModelSerializer):
    location = RestaurantLocationSerializers(
        many=False, source="Locations_person")

    class Meta:
        model = RestaurantAccount
        fields = ('id', 'added_by', 'name', 'address', 'city', 'country',
                  'Service', 'Categorie', 'bio', 'website', 'avatar', 'phone', 'status')


class PersonLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonLocations
        fields = ('id', 'added_by', 'long', 'lat')


class PersonPhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonPhone
        fields = ('id', 'added_by', 'phone', 'isActivate')


class PersonelAccountSerializer(serializers.ModelSerializer):
    location = PersonLocationSerializers(
        many=False, source="Person_location")
    phone = PersonPhoneSerializers(many=False, source="Person_phone")

    class Meta:
        model = PersonelAccount
        fields = ('id', 'added_by', 'name', 'address',
                  'city', 'country', 'location', 'phone', 'created_at', 'updated_at')


class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id', 'reviewed_by', 'rstr_id', 'rate',
                  'content', 'created_at', 'updated_at')


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'rated_by', 'rating', 'rate',
                  'delivery_rate', 'takeaway_rate', 'dinin_rate', 'created_at', 'updated_at')


class RatingSingleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'rate',
                  'delivery_rate', 'takeaway_rate', 'dinin_rate')
