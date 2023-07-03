from django.db import models

# Create your models here.


class AudioFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="audio/")
    size = models.IntegerField(default=0)
    Image=models.ImageField(upload_to="image/",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return self.title,self.file
    
    def get_file_upload_date(self):
        return self.created_at