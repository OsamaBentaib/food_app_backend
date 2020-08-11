from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import viewsets

import json
from django.core.exceptions import ObjectDoesNotExist

# Models And Serializers
from .models import *
from .serializers import *


# Get Personel Info
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_personel_info(request):
    user = request.user.id
    Person = PersonelAccount.objects.get(added_by=user)
    serializer = PersonelAccountSerializer(Person, many=False)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_token_type(request):
    user = request.user.id
    tokentype = TokenType.objects.get(user=user)
    serializer = TokenTypeSerializer(tokentype)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_token_type(request):
    payload = json.loads(request.body)
    author = request.user
    create = TokenType.objects.create(
        user=author,
        account=int(payload["account"]),
    )
    serializer = TokenTypeSerializer(create)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)

# POST Personel Info


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_personel_account(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        create = PersonelAccount.objects.create(
            added_by=user,
            name=payload["name"],
            address=payload["address"],
            city=payload["city"],
            country=payload["country"],
            phone=payload["phone"],
        )
        serializer = PersonelAccountSerializer(create)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# PUT Personel Info


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_personel_account(request, profile_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        Person_item = PersonelAccount.objects.filter(
            added_by=user, id=profile_id)
        # returns 1 or 0
        Person_item.update(**payload)
        Person = PersonelAccount.objects.get(id=profile_id)
        serializer = PersonelAccountSerializer(Person)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# DELETE Personel Info


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_personel_account(request, profile_id):
    user = request.user.id
    try:
        Profile = PersonelAccount.objects.get(added_by=user, id=profile_id)
        Profile.delete()
        return Response({"message": "success"}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Get Restaurant Info


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_restaurant_info(request):
    user = request.user
    Restaurant = RestaurantAccount.objects.get(added_by=user)
    serializer = RestaurantAccountAddSerializer(Restaurant)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_restaurant_profile(request):
    user = request.user
    Restaurant = RestaurantAccount.objects.get(added_by=user)
    serializer = RestaurantAccountSerializer(Restaurant)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_restaurant_with_id_profile(request, id):
    Restaurant = RestaurantAccount.objects.get(id=id)
    serializer = RestaurantAccountSerializer(Restaurant)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
# POST RESTAURANT INFO


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser, MultiPartParser, FormParser, FileUploadParser])
def add_restaurant_account(request, format=None):
    payload = json.loads(request.body)
    user = request.user
    try:
        create = RestaurantAccount.objects.create(
            added_by=user,
            name=payload["name"],
            address=payload["address"],
            phone=payload["phone"],
            Categorie=payload["Categorie"],
            bio=payload["bio"],
            website=payload["website"],
            avatar="",
        )
        serializer = RestaurantAccountAddSerializer(create)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# PUT Restaurant Info


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_restaurant_account(request):
    user = request.user
    payload = json.loads(request.body)
    try:
        restaurant_item = RestaurantAccount.objects.filter(
            added_by=user)
        # returns 1 or 0
        restaurant_item.update(**payload)
        restaurants = RestaurantAccount.objects.get(added_by=user)
        serializer = RestaurantAccountAddSerializer(restaurants)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# DELETE Restaurant Info


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_restaurant_account(request, profile_id):
    user = request.user.id
    try:
        Profile = RestaurantAccount.objects.get(added_by=user, id=profile_id)
        Profile.delete()
        return Response({"message": "success"}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# GET COUNTRIES LIST


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_countries_list(request):
    countr = Countries.objects.all()
    serializer = CountriesSerializer(countr, many=True)
    if countr.count() > 0:
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': "ObjectDoesNotExist"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_countries(request):
    payload = json.loads(request.body)
    try:
        create = Countries.objects.create(
            name=payload["name"],
        )
        serializer = CountriesSerializer(create)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# GET CITIES LIST


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_cities_list(request):
    citie = Cities.objects.all()
    serializer = CitiesSerializer(citie, many=True)
    if citie.count() > 0:
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': "ObjectDoesNotExist"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_cities(request):
    payload = json.loads(request.body)
    try:
        create = Cities.objects.create(
            name=payload["name"],
            country=payload["country"]
        )
        serializer = CitiesSerializer(create)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Service OFFER FOR RESTAURANT


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_service_offer(request, profile_id):
    seroffr = ServiceOffer.objects.get(rst_id=profile_id)
    serializer = ServiceOfferSerializer(seroffr, many=False)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_service_offer(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        author = RestaurantAccount.objects.get(added_by=user)
        create = ServiceOffer.objects.create(
            rst_id=author,
            isDelivery=payload["isDelivery"],
            isNcDelivery=payload["isNcDelivery"],
            isTakeaway=payload["isTakeaway"],
            isDinIn=payload["isDinIn"]
        )
        serializer = ServiceOfferAddSerializer(create)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_service_offer(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        author = RestaurantAccount.objects.get(added_by=user)
        service = ServiceOffer.objects.filter(rst_id=author)
        service.update(**payload)
        serializer = ServiceOfferAddSerializer(service)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_reviews(request, profile_id):
    reviews_list = Reviews.objects.filter(rstr_id=profile_id)
    serializer = ReviewsSerializers(reviews_list, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_reviews_check(request, profile_id):
    user = request.user.id
    reviews_list = Reviews.objects.filter(rstr_id=profile_id, reviewed_by=user)
    serializer = ReviewsSerializers(reviews_list, many=False)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_reviews(request, profile_id):
    payload = json.loads(request.body)
    user = request.user
    try:
        rst = RestaurantAccount.objects.get(id=profile_id)
        create = Reviews.objects.create(
            rstr_id=rst, reviewed_by=user, content=payload['content'], rate=payload['rate'],)
        serializer = ReviewsSerializers(create)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_reviews(request, profile_id):
    payload = json.loads(request.body)
    user = request.user.id

    try:
        review = Reviews.objects.filter(
            rstr_id=profile_id, reviewed_by=user)
        review.update(**payload)
        return JsonResponse({"message": "updated!"}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_reviews(request, profile_id):
    payload = json.loads(request.body)
    user = request.user.id
    try:
        review = Reviews.objects.filter(
            rstr_id=profile_id, reviewed_by=user)
        review.delete()
        return JsonResponse({"message": "deleted!"}, safe=False, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_rating(request, profile_id):
    rating_list = Rating.objects.filter(rating=profile_id)
    serializer = RatingSerializers(rating_list, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_rating_check(request, profile_id):
    user = request.user.id
    rating = Rating.objects.get(
        rating=profile_id, rated_by=user)
    serializer = RatingSerializers(rating)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_rating(request, profile_id):
    payload = json.loads(request.body)
    user = request.user
    try:
        rst = RestaurantAccount.objects.get(id=profile_id)
        create = Rating.objects.create(
            rating=rst, rated_by=user, rate=payload['rate'], delivery_rate=payload['delivery_rate'], takeaway_rate=payload['takeaway_rate'], dinin_rate=payload['dinin_rate'],)
        serializer = RatingSerializers(create)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_rating(request, profile_id):
    payload = json.loads(request.body)
    user = request.user.id
    try:
        rating = Rating.objects.filter(
            rating=profile_id, rated_by=user)
        rating.update(**payload)
        return JsonResponse({"message": "updated!"}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_rating(request, profile_id):
    payload = json.loads(request.body)
    user = request.user.id
    try:
        rating = Rating.objects.filter(
            rating=profile_id, rated_by=user)
        rating.delete()
        return JsonResponse({"message": "deleted!"}, safe=False, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_services(request):
    List = ServicesChoices.objects.filter()
    serializer = ServicesSerializers(List, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


# Restaurant Queries For Person

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_popular_list(request, city):
    user = request.user
    Restaurant = RestaurantAccount.objects.filter(city=city)
    serializer = RestaurantAccountSerializer(Restaurant, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
