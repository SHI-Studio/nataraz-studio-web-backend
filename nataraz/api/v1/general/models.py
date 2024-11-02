from django.db import models

class Media(models.Model):
    media_text = models.CharField(max_length=50)
    file = models.FileField(upload_to='media/general/')
    
    def __str__(self):
        return f"{self.media_text} - {self.file.name}"
