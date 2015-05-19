from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    rating = models.FloatField()

    def __str__(self):
        return "{} - {}".format(self.name, self.rating)

class Projection(models.Model):
    type = models.CharField(max_length = 5)
    data = models.CharField(max_length = 12)
    time = models.CharField(max_length = 12)
    movie = models.ForeignKey(Movies)

    def __str__(self):
        return "{} - {}".format(self.data, self.movie)
