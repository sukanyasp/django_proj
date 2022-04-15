from django.db import models

# Create your models here.
class User(models.Model):
    ssn = models.CharField(max_length=8)
    id = models.IntegerField
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.TextField(max_length=50)
    email = models.TextField()
    specialty = models.CharField(max_length=100)
    officelocation = models.TextField(max_length=50)
    sector = models.TextField()

    def __str__(self):
        return self.firstname
