from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    

class Books(models.Model):
    authors = models.ForeignKey(Author,related_name='written',on_delete=models.CASCADE)
    title = models.CharField(max_length = 255,unique=True)

    def __str__(self):
        return self.title
