from django.db import models


class UserUploadPhoto(models.Model):
    """
    Django database field.
    """
    image = models.ImageField(upload_to='user_upload_images/')
