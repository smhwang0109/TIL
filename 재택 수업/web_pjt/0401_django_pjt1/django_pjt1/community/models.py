from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    rank = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ],
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)