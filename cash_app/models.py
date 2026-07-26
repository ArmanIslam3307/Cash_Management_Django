from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class CustomUser(AbstractUser):

  full_name = models.CharField(max_length = 100, null=True)
  phone = models.PositiveIntegerField(null=True)

  def __str__(self):
    return self.username
      
class AddCash(models.Model):
  user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
  source = models.CharField(max_length=100,null=True)
  datetime = models.DateTimeField(null=True)
  amount = models.FloatField(null=True)
  description = models.TextField(null=True)


  def __str__(self):
    return self.amount
    
class Expense(models.Model):
  user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
  datetime = models.DateTimeField(null=True)
  amount = models.FloatField(null=True)
  description = models.TextField(null=True)


  def __str__(self):
    return self.amount
  


