from django.db import models

# Create your models here.
class Ticket(models.Model):
    Pax_Name        =   models.CharField(max_length=50)
    F_H_Name        =   models.CharField(max_length=50)
    Company_Name    =   models.CharField(max_length=50)
    Route           =   models.CharField(max_length=50)
    price           =   models.DecimalField(max_digits=8, decimal_places=2)
    profit_percent  =   models.DecimalField(max_digits=3, decimal_places=1)
    myshare         =   models.DecimalField(max_digits=8, decimal_places=2)
    Travel_agency   =   models.CharField(max_length=50)
    summary         =   models.TextField(default='This is Cool!')



