from django.db import models
from django.contrib.auth.models import user

# Create your models here.
TYPE=( 
    ('Positive','Positive'),
    ('Negative','negative')
)

class Profile(request):

class Expense(models.Model):
    name=models.charField(max_length=100)
    expense_type=models.CharField(max_length=100, choices=TYPE)

    def __str__(self):
        return self.name
