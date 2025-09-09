from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Review(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (0, 'Draft')
        PUBLISHED = (1, 'Published')

    class RatingChoices(models.IntegerChoices):
        BAD = (0, '0 - Bad')
        POOR = (1, '1 - Poor')
        FAIR = (2, '2 - Draft')
        GOOD = (3, '3 - Good')
        EXCELLENT = (4, '4 - Excellent')
        EXCEPTIONAL = (5, '5 - Exceptional')

    title = models.CharField(max_length=200)
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    body =  models.TextField()
    #Utiliza a class User já pronta em django.contrib.auth.models
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.GOOD)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.title} - {self.status}'


