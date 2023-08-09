from django.db import models

# Create your models here - version 4.
class Menu(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    inventory=models.IntegerField()
    
class Booking(models.Model):
    name=models.CharField(max_length=255)
    numberOfGuest=models.IntegerField()
    bookingDate=models.DateTimeField()
    