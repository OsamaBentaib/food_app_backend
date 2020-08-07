from django.contrib import admin
from .models import *

admin.site.register(PersonelAccount)
admin.site.register(RestaurantAccount)
admin.site.register(CategoriesChoices)
admin.site.register(ServiceOffer)
admin.site.register(ServicesChoices)
admin.site.register(Cities)
admin.site.register(Countries)
admin.site.register(Verifications)
admin.site.register(TokenType)
admin.site.register(Rating)

