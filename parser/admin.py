from django.contrib import admin
from .models import LinkedInProfile, JobExperience, JobSource, UserJobPreference, JobListing

admin.site.register(LinkedInProfile)
admin.site.register(JobExperience)

@admin.register(JobSource)
class JobSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'scraper_key', 'category', 'base_url')
    search_fields = ('name', 'scraper_key')

admin.site.register(UserJobPreference)
admin.site.register(JobListing)