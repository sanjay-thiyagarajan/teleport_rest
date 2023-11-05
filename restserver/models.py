from django.db import models
from drf_extra_fields.fields import Base64ImageField

genders = [("Male", "Male"), ("Female", "Female"), ("Others", "Others")]
status = [("pending", "pending"),
          ("in_progress", "in_progress"),
          ("completed", "completed"), ("cancelled", "cancelled")]


class Office(models.Model):
    office_location = models.CharField(max_length=500)
    office_name = models.CharField(max_length=500, primary_key=True)


class Person(models.Model):
    name = models.CharField(max_length=500)
    gender = models.CharField(max_length=10, choices=genders)
    home_location = models.CharField(max_length=500)
    work_pattern = models.CharField(max_length=500)
    email_address = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    profile_photo = models.TextField()

class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=500)
    vehicle_model = models.CharField(max_length=500)
    reg_number = models.CharField(max_length=10, choices=genders)
    mileage = models.IntegerField()
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    capacity_including_driver = models.IntegerField()


class PoolingRequestModel(models.Model):
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=50, choices=status)
