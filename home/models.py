from django.db import models
#makemigrations - create changes and store in a file.
#migrate - apply the pending changes created by make migrations.
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=50)
    phone = models.PositiveIntegerField()
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name
    
class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
class signup(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class welcome(models.Model):
    def __str__(self):
        return self.name
    