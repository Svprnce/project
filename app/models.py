from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Books(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title} By {self.author}'
    

class Fans(models.Model):
    name = models.CharField(max_length=15)
    fav_book = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return f'{self.name}'