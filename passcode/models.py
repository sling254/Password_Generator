from django.db import models

# Create your models here.

class PasswordGenearator(models.Model):
    username = models.CharField(max_length=50)
    site_name = models.CharField(max_length=50)
    length = models.CharField(max_length=10000)
    No_of_password = models.CharField(max_length=4000)

    def __str__(self):
        return self.username