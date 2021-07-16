from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField()
    flats = [
        ('A','Activo'),
        ('F','Finalizado')
    ]
    flat = models.CharField(max_length=1,choices=flats,default='A')

    def __str__(self):
        return "{} / {}".format(self.name,self.website)
