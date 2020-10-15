from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=240)
    image = models.ImageField(upload_to = 'project/images')
    link = models.URLField(blank = True)

    def __str__(self):
        return self.title