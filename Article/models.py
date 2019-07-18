from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'


class Type(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'types'


class Article(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateField(auto_now=True)
    content = RichTextField()
    description = RichTextField()
    picture = models.ImageField(upload_to='images')

    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    type = models.ManyToManyField(to=Type)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
