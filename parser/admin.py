from django.contrib import admin
from .models import LinkedInProfile, JobExperience, JobSource, UserJobPreference, JobListing

admin.site.register(LinkedInProfile)
admin.site.register(JobExperience)
admin.site.register(JobSource)
admin.site.register(UserJobPreference)
admin.site.register(JobListing)