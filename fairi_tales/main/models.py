from django.db import models

class Autor(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Story(models.Model):
    title=models.CharField(max_length=100)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='stories')
    genre =models.ManyToManyField(Genre, blank=True)
    content = models.TextField()
   # image = models.ImageField(upload_to='story_images/')

    def __str__(self):
        return self.title
