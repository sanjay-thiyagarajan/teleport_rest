from django.db import models

genders = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
status = [("pending", "pending"), ("in_progress", "in_progress"), ("completed", "completed"), ("cancelled", "cancelled")]


class Office(models.Model):
    office_location = models.CharField(max_length=500)
    office_name = models.CharField(max_length=500, primary_key=True)


class Person(models.Model):
    name = models.CharField(max_length=500)
    gender = models.CharField(max_length=10, options=genders)
    home_location = models.CharField(max_length=500)
    work_pattern = models.CharField(max_length=500)
    email_address = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    profile_photo = models.CharField(max_length=500)


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=500)
    vehicle_model = models.CharField(max_length=500)
    reg_number = models.CharField(max_length=10, options=genders)
    mileage = models.IntegerField()
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    capacity_including_driver = models.IntegerField()


class PoolingRequestModel(models.Model):
    sender = models.ForeignKey(Person, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, options=status)
