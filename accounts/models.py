from django.db import models
from django.conf import settings
from django.utils import timezone

# Create Personel user account models.


class Countries(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cities(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PersonLocations(models.Model):
    added_by = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)


class RestaurantLocations(models.Model):
    added_by = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)


class PersonelAccount(models.Model):
    added_by = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create Restaurant user account models.


class ServicesChoices(models.Model):
    service = models.CharField(max_length=300)
    adeed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service


class CategoriesChoices(models.Model):
    categorie = models.CharField(max_length=300)
    adeed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categorie


class RestaurantAccount(models.Model):
    added_by = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,)
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=200,)
    city = models.CharField(max_length=200,)
    country = models.CharField(max_length=200,)
    Service = models.CharField(max_length=200,)
    Categorie = models.CharField(max_length=200,)
    bio = models.TextField()
    website = models.CharField(max_length=200,)
    avatar = models.ImageField(
        upload_to='Profile', max_length=90000, blank=False, null=False)
    isVirefied = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ServiceOffer(models.Model):
    rst_id = models.OneToOneField(
        RestaurantAccount, on_delete=models.SET_NULL, null=True, related_name='serviceOfferType',)
    isDelivery = models.BooleanField(default=False)
    isNcDelivery = models.BooleanField(default=False)
    isTakeaway = models.BooleanField(default=False)
    isDinIn = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Verifications(models.Model):
    rst_id = models.ForeignKey(
        RestaurantAccount, on_delete=models.SET_NULL, null=True, related_name='rst_Verification',)
    isVirefied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TokenType(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account = models.IntegerField()


class Rating(models.Model):
    rated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.ForeignKey(
        RestaurantAccount, on_delete=models.SET_NULL, null=True)
    delivery_rate = models.DecimalField(max_digits=2, decimal_places=1)
    takeaway_rate = models.DecimalField(max_digits=2, decimal_places=1)
    dinin_rate = models.DecimalField(max_digits=2, decimal_places=1)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reviews(models.Model):
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rstr_id = models.ForeignKey(
        RestaurantAccount, on_delete=models.SET_NULL, null=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
