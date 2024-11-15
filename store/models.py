from django.db import models
import uuid

class Product(models.Model):
    #sku = models.CharField(max_length=10, primary_key=True) # primary key
    title = models.CharField(max_length=255) # only required parameter
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places = 2) # use decimal over float to prevent rounding errors. 4 digits (9999) and 2 d.p (.99)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B' # better practice than just using the letters themselves, as these can be modified quicker
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'


    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze') # dropdown list later
        (MEMBERSHIP_SILVER, 'Silver')
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    first_name = models.CharField(max_length = 63)
    last_name = models.CharField(max_length= 63)
    email = models.EmailField(unique=True)
    phone = models.CharField()
    birth_date = models.DateField(null = True)
    membership = models.CharField(max_length = 1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Models):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_CHOICES = [
        (PAYMENT_PENDING, 'Pending') # dropdown list later
        (PAYMENT_COMPLETE, 'Complete')
        (PAYMENT_FAILED, 'Failed')
    ]

    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_PENDING)
