from django.db import models
from django.conf import settings

class LinkedInProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="linkedin_profile"
    )
    full_name = models.CharField(max_length=255, blank=True)
    headline = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    current_position = models.CharField(max_length=255, blank=True)
    last_synced = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s LinkedIn Profile"
    

class JobExperience(models.Model):
    profile = models.ForeignKey(LinkedInProfile, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    start_date = models.CharField(max_length=50, blank=True)  # Free text for now
    end_date = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} at {self.company}"