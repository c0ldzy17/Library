from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth date')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:author_info', args=[self.id])


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publication date')

    def __str__(self):
        return f"{str(self.author)}. {self.title}"

    def get_absolute_url(self):
        return reverse('books:book_info', args=[self.pk])