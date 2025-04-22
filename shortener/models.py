from django.db import models


class ShortURL(models.Model):
    """ShortURL model"""

    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True)
