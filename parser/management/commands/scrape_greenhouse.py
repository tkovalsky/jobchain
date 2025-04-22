from django.core.management.base import BaseCommand
from parser.models import JobSource, JobListing
from scrapers.greenhouse import scrape_greenhouse_jobs

class Command(BaseCommand):
    help = 'Scrapes Greenhouse job boards'

    def handle(self, *args, **options):
        sources = JobSource.objects.filter(source_type="greenhouse")

        for source in sources:
            jobs = scrape_greenhouse_jobs(source.base_url)
            for job in jobs:
                listing, created = JobListing.objects.get_or_create(
                    internal_id=f"{source.id}-{job['external_id']}",
                    defaults={
                        "external_id": job["external_id"],
                        "source": source,
                        "title": job["title"],
                        "company": job["company"],
                        "location": job["location"],
                        "url": job["url"],
                        "description": "",
                    }
                )
                if not created:
                    listing.times_seen += 1
                    listing.save()