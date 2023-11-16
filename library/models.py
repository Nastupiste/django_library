from datetime import timezone
from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    sinopsis = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
