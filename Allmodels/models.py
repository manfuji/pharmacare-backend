from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


class Categories(models.Model):
    catName = models.CharField(max_length=250)
    createdAt = models.DateTimeField(auto_now=True, auto_now_add=False)
    updatedAt = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.catName


class Product(models.Model):
    options = (
        ("AVAILABLE", "AVAILABLE"),
        ("UNAVAILABLE", "UNAVAILABLE")
    )

    def upload_location(instance, filename):
        return 'product/{filename}'.format(filename=filename)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    productName = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(
        choices=options, max_length=50, default="AVAILABLE")
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=250)
    image = models.ImageField(
        _("Image"), upload_to=upload_location, blank=True, null=True)
    slug = models.SlugField()
    discount = models.CharField(max_length=50, default="20")
    createdAt = models.DateTimeField(auto_now=True, auto_now_add=False)
    updatedAt = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.productName


class Profile(models.Model):
    def upload_location(instance, filename):
        return 'profile/{filename}'.format(filename=filename)

    profileUser = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    profileImage = models.ImageField(
        _("Image"), upload_to=upload_location, blank=True, null=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updatedAt = models.DateTimeField(auto_now=True, auto_now_add=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(profileUser=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.profileUser.username


class Order(models.Model):
    options = (
        ("PAID", "PAID"),
        ("PENDING", "PENDING"),
        ("PAYONDELIVERY", "PAYONDELIVERY")
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    orderTime = models.DateTimeField(auto_now=True, auto_now_add=False)
    payment = models.CharField(
        choices=options, max_length=50, default="PENDING")
    orderComplete = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username
