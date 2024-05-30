from django.db import models

# Create your models here.
class accInfo(models.Model):
    username = models.CharField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username
