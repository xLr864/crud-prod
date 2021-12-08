from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    ratting = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    verdict = models.TextField() 