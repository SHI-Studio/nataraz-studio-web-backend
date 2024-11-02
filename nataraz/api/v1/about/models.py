from django.db import models

class ExtraData(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=255)
    extra_data = models.ManyToManyField(ExtraData, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Nataraz About"
        unique_together = (('title',),)
    