from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.TimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title