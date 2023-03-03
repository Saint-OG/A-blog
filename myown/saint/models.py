from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50)
    matric = models.IntegerField()
    sex = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Sex = models.CharField(max_length=1, choices=sex, default='M')
    phone_number = models.IntegerField(null=True)

