# Generated by Django 4.0.4 on 2022-05-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0008_jobskill_remove_job_primary_skills_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobskill',
            name='is_mandatory',
            field=models.BooleanField(default=True),
        ),
    ]