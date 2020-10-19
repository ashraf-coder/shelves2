from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=30)
    NIN = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)
    dealers_in = models.TextField(null=True)

    def __str__(self):
        return self.business_name


class Phone(models.Model):
    image = ResizedImageField(size=[500, 500],default='', blank=True, upload_to="images")
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    RAM = models.CharField(max_length=20)
    storage = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    addedBy = models.ForeignKey("Business", null=True, on_delete=models.CASCADE)
    addedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Laptop(models.Model):
    name = models.CharField(max_length=20)
    storage = models.CharField(max_length=20)
    RAM = models.CharField(max_length=20)
    addedBy = models.ForeignKey("Business", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Shoe(models.Model):
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=20, default=None)
    maker = models.CharField(max_length=20, default=None)
    addedBy = models.ForeignKey("Business", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=10, null=True)
    productName = models.CharField(max_length=30)
    business = models.ForeignKey("Business", null=True, on_delete=models.CASCADE)
    addedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name