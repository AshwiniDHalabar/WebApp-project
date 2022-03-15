from django.db import models

# Create your models here.

class user(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=200)
    confirmpassword = models.CharField(max_length=200)
    

    def __str_(self):
        return self.title