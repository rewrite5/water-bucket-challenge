from django.db import models

# Create your models here.

from django.db import models


class WaterBucket(models.Model):
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    z = models.PositiveIntegerField()

    def __str__(self):
        return f"Water Bucket {self.x} {self.y} {self.z}"
