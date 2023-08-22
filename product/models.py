from django.db import models

# Create your models here.
class productcls(models.Model):
    onvan=models.CharField(max_length=100)
    gheymat=models.CharField(max_length=20)
    tosif=models.TextField(max_length=40)
    aks=models.CharField(max_length=20) 

    def __str__(self):
        return self.onvan