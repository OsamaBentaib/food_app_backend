from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import *
from rest_framework import status

from .models import *
from accounts.models import RestaurantAccount
import json
from django.core.exceptions import ObjectDoesNotExist


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_menu_list(request, rst_id):
    List = MenuItem.objects.filter(rst_id=rst_id)
    serializer = MenuItemDetailsSerializer(List, many=True)
    if List.count() > 0:
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    else:
        return JsonResponse({"error": "Not Found"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_menu_item_details(request, item_id):
    List = MenuItem.objects.get(id=item_id)
    serializer = MenuItemDetailsSerializer(List, many=False)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_menu_item(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        author = RestaurantAccount.objects.get(added_by=user)
        item = MenuItem.objects.create(
            added_by=user,
            rst_id=author,
            title=payload["title"],
            description=payload["description"],
            price=payload["price"],
            dprice=payload["dprice"],
            categories=payload["categories"],
            poster="",
        )
        serializer = MenuItemSerializer(item)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_menu_item(request, item_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        menu_item = MenuItem.objects.filter(added_by=user, id=item_id)
        # returns 1 or 0
        menu_item.update(**payload)
        book = MenuItem.objects.get(id=item_id, added_by=user)
        serializer = MenuItemSerializer(book)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_menu_item(request, item_id, profile_id):
    user = request.user.id
    try:
        items = MenuItem.objects.get(added_by=user, id=item_id)
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
