# Generated by Django 5.2 on 2025-04-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parser", "0005_rename_source_type_jobsource_scraper_key_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobsource",
            name="scraper_key",
            field=models.CharField(
                help_text="Internal scraper ID (e.g. 'greenhouse', 'lever'). Used for backend routing only.",
                max_length=50,
            ),
        ),
    ]
