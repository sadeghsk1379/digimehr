from django.db import models

from accounts.models import CustomUser


class Institute(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    

class plan(models.Model):

    name = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    Institute_of_plan = models.ForeignKey(Institute,on_delete=models.CASCADE)

class UserAccount(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)

    
