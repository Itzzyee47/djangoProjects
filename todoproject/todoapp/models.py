from django.db import models

# Create your models here.
class task(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=255)
    set_date = models.DateField()
    
    def __str__(self):
        return  f"{self.id},{self.title}, {self.discription}, {self.set_date}"