from django.conf.urls import url
from django.urls import include, path
from .views import *

urlpatterns = [
    path('person/all/', get_person_orders),
    path('restaurant/<int:rst>/order/create/',
         create_order),
    path('restaurant/<int:rst>/order/<int:order>/item/create/',
         create_order_item),
    path('restaurant/<int:rst>/order/<int:order>/update/',
         update_order_by_person),

    path('restaurant/person/<int:person>/order/<int:order>/',
         update_order_by_restaurant),

    path('restaurant/all/order/<int:order>/start/<int:start>/end/<int:end>/',
         get_restaurant_orders_all),
    path('restaurant/<str:p>/s/<str:s>/<int:start>/<int:end>/',
         get_restaurant_orders_lists),

    # path('addbook', add_book),
    # path('updatebook/<int:book_id>', update_book),
    # path('deletebook/<int:book_id>', delete_book)
]
