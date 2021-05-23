from django.db import models
from django.utils import timezone

class Advert(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    phoneNumber = models.IntegerField()
    posterName = models.CharField(max_length=100)
    pubDate = models.DateTimeField(default = timezone.now)
    city = models.CharField(max_length=20)
    featured = models.BooleanField(null = True)
    viewsAmount = models.IntegerField(default = 0)
    def getAbsoluteUrl(self):
        return f"/vacancy/{self.id}/"