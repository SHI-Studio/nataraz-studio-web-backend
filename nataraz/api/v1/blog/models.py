from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='media/blog_covers/')
    author = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category, related_name='blogs')

    def __str__(self):
        return self.title

class Paragraph(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='paragraphs')
    title = models.CharField(max_length=255)
    content = RichTextField()

    def __str__(self):
        return self.title
