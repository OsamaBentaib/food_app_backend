from django.conf.urls import url 
from django.urls import include, path
from .views import * 
 
urlpatterns = [ 
    # url(r'^api/tutorials$', tutorial_list),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', tutorial_detail),
    # url(r'^api/tutorials/published$', tutorial_list_published),
    path('getbooks', get_books),
    path('addbook', add_book),
    path('updatebook/<int:book_id>', update_book),
    path('deletebook/<int:book_id>', delete_book)
]