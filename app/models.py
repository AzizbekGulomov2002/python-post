from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.


class Post(models.Model):
    sarlavha = models.CharField(max_length=50)
    malumot = models.TextField()
    rasm = models.ImageField(upload_to='post_image',null=True,blank=True)
    video = models.FileField(upload_to='post_video',null=True,blank=True)
    kurishlar = models.IntegerField(default=1)
    def __str__(self):
        return self.sarlavha
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
    