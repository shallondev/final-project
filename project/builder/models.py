from django.db import models
from django.contrib.auth.models import AbstractUser


BUILDING_ZONES = [
    ("RESIDENTIAL", "Residential"), 
    ("COMMERCIAL", "Commercial"),  
    ("INDUSTRIAL", "Industrial"),
]

TRANSPORT_TYPES = [
    ("ROAD", "Road"),
    ("TRACKS", "Tracks"),
    ("PATH", "Path"),
]

class User(AbstractUser):
    pass

class City(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=50)
    population = models.IntegerField(default=0)
    buildings = models.ManyToManyField('Building', related_name='city')
    transports = models.ManyToManyField('Transport', related_name='city')
    schools = models.ManyToManyField('School', related_name='city')
    hospitals = models.ManyToManyField('Hospital', related_name='city')
    police_stations = models.ManyToManyField('PoliceStation', related_name='city')
    fire_departments = models.ManyToManyField('FireDepartment', related_name='city')

class Transport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    transport_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, choices=TRANSPORT_TYPES)

class Building(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    building_id = models.AutoField(primary_key=True)
    zone = models.CharField(max_length=50, choices=BUILDING_ZONES)

class School(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    school_id = models.AutoField(primary_key=True)

class Hospital(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    hospital_id = models.AutoField(primary_key=True)  

class PoliceStation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    police_station_id = models.AutoField(primary_key=True)

class FireDepartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    fire_id = models.AutoField(primary_key=True)

