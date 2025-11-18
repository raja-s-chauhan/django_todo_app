from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images' , blank=True, null=True)
    designation = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=254)
    phone_number = models.CharField(max_length=12,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.designation}"