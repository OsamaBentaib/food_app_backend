from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('core/', include('core.urls')),
    # Accounts
    path('api/', include('accounts.urls')),
    # menu
    path('api/menu/', include('menu.urls')),
    # orders
    path('api/orders/', include('orders.urls')),
    # admin
    path('admin/', admin.site.urls),
]
