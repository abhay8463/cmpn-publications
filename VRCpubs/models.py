from django.db import models
from time import strftime

# Create your models here.





class VRCPubs(models.Model):

    title = models.CharField(max_length=1000)

    category = models.CharField(max_length=100)

    author= models.CharField(max_length=100)

    link= models.URLField()

    publishedAt=models.DateTimeField()

    isbn= models.CharField(max_length=100)

    
    def __str__(self):
        return self.title

    def yearpublished(self):
        return self.publishedAt.strftime('%Y')
    
