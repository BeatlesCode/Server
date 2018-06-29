

# Create your models here.
from django.db import models

class UploadModel(models.Model):
    uploadfile = models.FileField(upload_to="media/music");


# class UploadModel(models.Model):
#      uploadfile = models.FileField();
#      fileName = models.CharField(max_length='100');