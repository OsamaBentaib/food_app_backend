from django.urls import include, path
from .views import *

urlpatterns = [
    path('token/', get_token_type),
    path('token/add/', add_token_type),
    path('account/personel/', get_personel_info),
    path('account/personel/add/', add_personel_account),
    path('account/personel/<int:profile_id>/update/', update_personel_account),
    path('account/personel/<int:profile_id>/delete/', delete_personel_account),
    path('account/restaurant/<int:id>/profile/',
         get_restaurant_with_id_profile),

    path('account/restaurant/', get_restaurant_info),
    path('account/restaurant/profile/', get_restaurant_profile),
    path('account/restaurant/add/', add_restaurant_account),
    path('account/restaurant/update/', update_restaurant_account),
    path('account/restaurant/delete/', delete_restaurant_account),
    path('account/restaurant/<int:profile_id>/serviceoffer/', get_service_offer),
    path('account/restaurant/serviceoffer/add/', add_service_offer),
    path('account/restaurant/serviceoffer/update/', update_service_offer),

    path('account/restaurant/<int:profile_id>/reviews/', get_reviews),
    path('account/restaurant/<int:profile_id>/reviews/check/', get_reviews_check),

    path('account/restaurant/<int:profile_id>/rating/', get_rating),

    path('lists/countries/', get_countries_list),
    path('lists/countries/add/', add_countries),
    path('lists/cities/', get_cities_list),
    path('lists/cities/add/', add_cities),
    path('lists/services/', get_services),

    #   path('addbook', add_book),
    #   path('updatebook/', update_book),
    #   path('deletebook/<int:book_id>', delete_book)
]
