from django.db import models

# Create your models here.


class Rate(models.Model):
    term = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=5, decimal_places=4)
    apr = models.DecimalField(max_digits=5, decimal_places=4, null=True)

    def __str__(self):
        return str(self.rate)
