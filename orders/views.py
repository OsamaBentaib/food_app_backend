from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F

from .serializers import *
from rest_framework import status

from .models import *
from accounts.models import PersonelAccount
import json
from django.core.exceptions import ObjectDoesNotExist


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_person_orders(request):
    user = request.user.id
    orders = Orders.objects.filter(ordered_by=user)
    serializer = OrdersSerializers(orders, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_restaurant_orders_all(request, start, end, order):
    user = request.user.id
    if order == 0:
        orfl = "-created_at"
    elif order == 1:
        orfl = "created_at"
    rst = RestaurantAccount.objects.get(added_by=user)
    orders = Orders.objects.filter(
        ordered_from=rst).order_by(orfl)[start:end]
    serializer = OrdersSerializers(orders, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_restaurant_orders_lists(request, s, p, start, end):
    user = request.user.id
    rst = RestaurantAccount.objects.get(added_by=user)
    if p == "all":
        if s == "all":
            orders = Orders.objects.filter(
                ordered_from=rst).order_by("-created_at")[start:end]
        else:
            orders = Orders.objects.filter(
                ordered_from=rst, order_status=s).order_by("-created_at")[start:end]
    if p == "delivery":
        if s == "all":
            orders = Orders.objects.filter(
                ordered_from=rst, order_type="DELIVERY").order_by("-created_at")[start:end]
        else:
            orders = Orders.objects.filter(
                ordered_from=rst, order_type="DELIVERY", order_status=s).order_by("-created_at")[start:end]
    if p == "takeaway":
        if s == "all":
            orders = Orders.objects.filter(
                ordered_from=rst, order_type="TAKEAWAY").order_by("-created_at")[start:end]
        else:
            orders = Orders.objects.filter(
                ordered_from=rst, order_type="TAKEAWAY", order_status=s).order_by("-created_at")[start:end]
    if p == "dinin":
        if s == "all":
            orders = Orders.objects.filter(
                ordered_from=rst, order_type="DININ").order_by("-created_at")[start:end]
        else:
            orders = Orders.objects.filter(
                ordered_from=rst, order_type="DININ", order_status=s).order_by("-created_at")[start:end]
    serializer = OrdersSerializers(orders, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_order(request, rst):
    payload = json.loads(request.body)
    user = request.user
    rest = RestaurantAccount.objects.get(id=rst)
    author = PersonelAccount.objects.get(added_by=user)
    order = Orders.objects.create(
        ordered_by=user,
        ordered_by_name=author,
        ordered_from=rest,
        order_type=payload['order_type'],
        order_time=payload['order_time'],
        order_status=payload['order_status'],
    )
    serializerNew = OrdersNewSerializers(order)
    serializerReturn = OrdersIdSerializers(order)
    return JsonResponse(serializerReturn.data, safe=False, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_order_item(request, order, rst):
    payload = json.loads(request.body)
    item = MenuItem.objects.get(id=payload['order_item'])
    id_ = Orders.objects.get(id=order)
    order = OrderItems.objects.create(
        order=id_,
        order_item=item,
        quantity=payload['quantity'],
    )
    serializer = OrderItemsNewSerializers(order)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_order_by_person(request, rst, order):
    payload = json.loads(request.body)
    user = request.user
    rest = RestaurantAccount.objects.get(id=rst)
    author = PersonelAccount.objects.get(added_by=user)
    __order = Orders.objects.filter(id=order, ordered_by=user)
    if payload['order_status'] == "SUBMITED":
        __order.update(
            order_status=payload['order_status'],
        )
    return JsonResponse({"updated": True}, safe=False, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_order_by_restaurant(request, person, order):
    payload = json.loads(request.body)
    user = request.user
    author = PersonelAccount.objects.get(id=person)
    __order = Orders.objects.filter(id=order, ordered_by_name=author)
    if payload['order_status'] == "CONFIRMED":
        __order.update(
            order_status=payload['order_status'],
        )
    if payload['order_status'] == "READY":
        __order.update(
            order_status=payload['order_status'],
        )
    if payload['order_status'] == "CANCLED":
        __order.update(
            order_status=payload['order_status'],
        )
    if payload['order_status'] == "FINISHED":
        __order.update(
            order_status=payload['order_status'],
        )
        RestaurantAccount.objects.filter(
            id=author).update(score=F('score') + 1)

    return JsonResponse({"updated": True}, safe=False, status=status.HTTP_201_CREATED)
    # try:
    # except ObjectDoesNotExist as e:
    #     return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    # except Exception:
    #     return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(["PUT"])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def update_book(request, book_id):
#     user = request.user.id
#     payload = json.loads(request.body)
#     try:
#         book_item = Book.objects.filter(added_by=user, id=book_id)
#         # returns 1 or 0
#         book_item.update(**payload)
#         book = Book.objects.get(id=book_id)
#         serializer = BookSerializer(book)
#         return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
#     except ObjectDoesNotExist as e:
#         return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#     except Exception:
#         return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(["DELETE"])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def delete_book(request, book_id):
#     user = request.user.id
#     try:
#         book = Book.objects.get(added_by=user, id=book_id)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     except ObjectDoesNotExist as e:
#         return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#     except Exception:
#         return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
