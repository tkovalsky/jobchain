import hashlib

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
    
class JobSource(models.Model):
    name = models.CharField(max_length=100)  # e.g. "Figma"
    base_url = models.URLField()  # e.g. "https://boards.greenhouse.io/figma"
    scraper_key = models.CharField(max_length=50, help_text="Internal scraper ID (e.g. 'greenhouse', 'lever'). Used for backend routing only.")
    category = models.CharField(max_length=100, blank=True, help_text="Optional: Job Board, Company Site, etc.")

    def __str__(self):
        return f"{self.name} ({self.scraper_key})"


class UserJobPreference(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_titles = models.TextField(help_text="Comma-separated list of job titles")
    locations = models.TextField(help_text="Comma-separated list of cities or states")
    radius_miles = models.IntegerField(default=25)
    sources = models.ManyToManyField(JobSource)

    def __str__(self):
        return f"{self.user.username}'s job preferences"
    

class JobListing(models.Model):
    source = models.ForeignKey(JobSource, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=255)  # ID from the source site
    internal_id = models.CharField(max_length=255, unique=True)  # hashed combo
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    url = models.URLField()
    description = models.TextField(blank=True)

    last_seen = models.DateTimeField(auto_now=True)
    times_seen = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.internal_id:
            # Generate a unique hash from source + external_id
            raw = f"{self.source.id}-{self.external_id}"
            self.internal_id = hashlib.sha256(raw.encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} @ {self.company} ({self.location})"