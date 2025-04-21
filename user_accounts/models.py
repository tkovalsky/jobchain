from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_unemployed = models.BooleanField(default=False)
    headline = models.CharField(max_length=255, blank=True)
    linkedin_url = models.URLField(blank=True)
    