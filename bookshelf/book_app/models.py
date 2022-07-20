from django.db import models


# In this case, I went with a one to many relationship
# Each book belongs to one genre, genres have many books
class Genre(models.Model):
    name = models.CharField(max_length = 255, blank = False)

class Book(models.Model):
    title = models.CharField(max_length = 255, blank = False)
    author = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE, default = 1)
