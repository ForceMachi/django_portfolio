from django.db import models


class Project(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='my_portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.tittle
