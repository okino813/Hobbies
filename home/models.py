from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    slug = models.CharField(max_length=100)


    def __str__(self):
        return self.title

