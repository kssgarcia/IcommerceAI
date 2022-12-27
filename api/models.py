from django.db import models
from users.models import User

# Create your models here.

class ImageModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(default='Untitled')
    image = models.ImageField(upload_to='files', null=False)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def delete(self, using=None, keep_parents=False):
        self.file.storage.delete(self.image.name)
        super().delete()

    def __str__(self):
        return self.name

    class meta():
        ordering = ['-create']

