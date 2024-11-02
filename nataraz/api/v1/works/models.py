from django.db import models
from api.v1.services.models import Service

class Work(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='media/work_covers/', blank=True, null=True)
    video = models.FileField(upload_to='media/work_videos/', blank=True, null=True)
    category = models.ManyToManyField(Service, related_name='works')
    date = models.IntegerField()
    contributor = models.ManyToManyField('Contributor', blank=True, related_name='works')

    def __str__(self):
        return self.title

class Contributor(models.Model):
    fullname = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname

class ExtraData(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    work = models.ForeignKey(Work, related_name='extra_data', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to='media/work_images/')
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='images')
    image_type = models.CharField(max_length=10, choices=[('full', 'Full'), ('half', 'Half')])

    def __str__(self):
        return self.title