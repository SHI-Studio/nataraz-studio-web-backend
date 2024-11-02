from django.db import models

class Testimonial(models.Model):
    title = models.CharField(max_length=255)
    response = models.TextField()
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial_images/')

    def __str__(self):
        return self.title
