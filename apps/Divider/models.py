from django.db import models
import os, uuid

def upload_to(instance, filename):
    base_name = os.path.splitext(filename)[0]
    name = 'original '+filename
    unique_folder_name = f"{base_name}_{uuid.uuid4().hex[:8]}"
    return os.path.join(unique_folder_name, name)

class ImageModel(models.Model):
    img = models.ImageField(blank=False, null=False, upload_to=upload_to)

    class Meta:
        verbose_name = 'ImageModel'
        verbose_name_plural = 'ImageModels'

