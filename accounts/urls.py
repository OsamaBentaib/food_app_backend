from django.urls import include, path
from .views import *

urlpatterns = [
    path('account/personel/phone/add/code/<int:code>/',
         add_personel_account_phone),
    path('account/personel/phone/update/', update_personel_account_phone),
    path('token/', get_token_type),
    path('token/add/', add_token_type),
    path('account/personel/', get_personel_info),
    path('account/personel/add/', add_personel_account),
    path('account/personel/<int:profile_id>/update/', update_personel_account),
    path('account/personel/<int:profile_id>/delete/', delete_personel_account),
    path('account/restaurant/<int:id>/profile/',
         get_restaurant_with_id_profile),
    path('account/person/location/add/', add_Location_person),
    path('account/person/location/update/', update_location_person),

    path('account/restaurant/', get_restaurant_info),
    path('account/restaurant/profile/', get_restaurant_profile),
    path('account/restaurant/add/', add_restaurant_account),
    path('account/restaurant/update/', update_restaurant_account),
    path('account/restaurant/delete/', delete_restaurant_account),
    path('account/restaurant/<int:profile_id>/serviceoffer/', get_service_offer),
    path('account/restaurant/serviceoffer/add/', add_service_offer),
    path('account/restaurant/serviceoffer/update/', update_service_offer),
    path('account/restaurant/location/add/', add_Location),
    path('account/restaurant/location/update/', update_location),

    path('account/restaurant/<int:profile_id>/reviews/', get_reviews),
    path('account/restaurant/<int:profile_id>/reviews/check/', get_reviews_check),
    path('account/restaurant/<int:profile_id>/reviews/add/', add_reviews),
    path('account/restaurant/<int:profile_id>/reviews/update/', update_reviews),
    path('account/restaurant/<int:profile_id>/reviews/delete/', delete_reviews),

    path('account/restaurant/<int:profile_id>/rating/', get_rating),
    path('account/restaurant/<int:profile_id>/rating/check/', get_rating_check),
    path('account/restaurant/<int:profile_id>/rating/add/', add_rating),
    path('account/restaurant/<int:profile_id>/rating/update/', update_rating),
    path('account/restaurant/<int:profile_id>/rating/delete/', delete_rating),

    path('lists/countries/', get_countries_list),
    path('lists/countries/add/', add_countries),
    path('lists/cities/', get_cities_list),
    path('lists/cities/add/', add_cities),
    path('lists/services/', get_services),



    # Filters by Lists
    path('fliters/list/c/<str:city>/', get_popular_list),
    path('fliters/list/takeaway/c/<str:city>/', get_takeaway_list),
    path('fliters/list/verified/c/<str:city>/', get_Verified_list),
    path('fliters/list/dinin/c/<str:city>/', get_dinIn_list),
    path('fliters/list/delivery/c/<str:city>/', get_delivery_list),
    path('fliters/list/open/c/<str:city>/', get_open_list),
    path('fliters/list/score/c/<str:city>/', get_score_list),
    path('fliters/list/promo/c/<str:city>/', get_promo_list),

    path('cities/json/query/<str:query>/',
         get_cities_list_json, name="Cities Json"),






    #   path('addbook', add_book),
    #   path('updatebook/', update_book),
    #   path('deletebook/<int:book_id>', delete_book)
]
