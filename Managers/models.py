from django.db import models

# Create your models here.
class Managers(models.Model):
    name=models.CharField(max_length=32)
    id_number=models.IntegerField()
    image=models.ImageField()
    worktime=models.DecimalField(max_digits=8,decimal_places=2)
    salary=models.IntegerField()
    description=models.TextField()
    date_hired=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
def __str__(self):
        return self.name  