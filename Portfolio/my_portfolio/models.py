from django.db import models
from PIL import Image

class Images(models.Model):
    image = models.ImageField(upload_to='images/')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        max_size = (300, 300)

        img.thumbnail(max_size)

        img.save(self.image.path)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
