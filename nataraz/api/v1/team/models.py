from django.db import models

class Member(models.Model):
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team_images/')
    linkedin_url = models.URLField()

    def __str__(self):
        return self.title

class ExtraData(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
