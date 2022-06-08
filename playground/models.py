from django.db import models

# Create your models here.

class People(models.Model):
    username = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Address(models.Model):
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    zip_code = models.CharField(max_length=100)
    patient = models.OneToOneField(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.state

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=1000)
    hospital_name = models.CharField(max_length=1000)
    patient = models.OneToOneField(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=1000)
    price = models.CharField(max_length=1000000)

    def __str__(self):
        return self.name

class Bio(models.Model):
    about = models.CharField(max_length=10000)
    user = models.OneToOneField(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.about


