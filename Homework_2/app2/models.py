from django.db import models

# Create your models here.


class Film(models.Model):

    name = models.CharField(max_length=40)
    description = models.TextField()
    release_year = models.IntegerField()
    lenght = models.IntegerField()
    sp_feature = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.release_year})"


class Actor(models.Model):

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    description = models.TextField()
    age = models.IntegerField()
    married = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}-{self.surname}"

GENRE_CHOICES  = (
                (0, "Action"),
                (1, "Drama"),
                (2, "Fantasy"),
                )

class Genre(models.Model):
    name = models.IntegerField(GENRE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return f"{GENRE_CHOICES[self.name][1]}"


class Movie(models.Model):

    name = models.CharField(max_length=20)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f"{self.name}--{self.genre}"