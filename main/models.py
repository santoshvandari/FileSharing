from django.db import models
from main.slugGenerator import slug_generator,fileid

# Create your models here.

class SharedFiles(models.Model):
    file = models.FileField(upload_to='uploads/')
    filename=models.CharField(max_length=100,blank=False)
    slug=models.SlugField(max_length=100, unique=True)
    fileid=models.CharField(max_length=100, unique=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    expiration_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.slug=slug_generator(self.title)
        self.fileid=fileid()
        if not self.expiration_time:
            self.expiration_time = timezone.now() + timedelta(hours=24)
        super().save(*args, **kwargs)



    def is_expired(self):
        return timezone.now() > self.expiration_time