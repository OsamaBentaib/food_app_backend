from django.conf.urls import url
from django.urls import include, path
from .views import *

urlpatterns = [
    # url(r'^api/tutorials$', tutorial_list),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', tutorial_detail),
    # url(r'^api/tutorials/published$', tutorial_list_published),
    path('items/restaurant/<int:rst_id>/lists/', get_menu_list),
    path('items/restaurant/list/<int:item_id>/details/', get_menu_item_details),
    path('items/restaurant/list/add/', add_menu_item),
    path('items/restaurant/list/<int:item_id>/update/', update_menu_item),
    path('items/restaurant/list/<int:item_id>/delete/', delete_menu_item),

    path('items/restaurant/list/<int:item>/intg/add/', add_menu_item_intG),
    path('items/restaurant/list/<int:item>/intg/', get_menu_item_inGt),
    path('items/restaurant/list/<int:item>/intg/<int:intg>/update/',
         update_menu_item_intG),
    path('items/restaurant/list/<int:item>/intg/<int:intg>/delete/',
         delete_menu_item_intG),
    # path('addbook', add_book),
    # path('updatebook/<int:book_id>', update_book),
    # path('deletebook/<int:book_id>', delete_book)
]
