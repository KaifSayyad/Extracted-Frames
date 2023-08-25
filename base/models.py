from django.db import models
from django.utils.text import slugify
# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100, null=True)
    image= models.ImageField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return str(self.title) + ": " + str(self.image)