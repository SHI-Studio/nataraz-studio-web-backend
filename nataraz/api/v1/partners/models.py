from django.db import models

class Partner(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/partner_logos/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
