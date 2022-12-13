from django.db import models


# Create your models here.
class Blog(models.Model):
    tittle = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.tittle
