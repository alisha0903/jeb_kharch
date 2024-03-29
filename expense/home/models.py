from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE=( 
    ('Positive','Positive'),
    ('Negative','negative')
)

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    income=models.FloatField(default=0)
    expense=models.FloatField(default=0)
    balance=models.FloatField(null=True,blank=True,default=0)

class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    amount=models.FloatField()
    expense_type=models.CharField(max_length=100, choices=TYPE)

    def __str__(self):
        return self.name
