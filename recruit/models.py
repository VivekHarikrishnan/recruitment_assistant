from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=75)
    code = models.CharField(max_length=3)


class Skill(models.Model):
    name = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    primary_skills = models.ManyToManyField(Skill, related_name="job_primary_skills")
    secondary_skills = models.ManyToManyField(Skill, related_name="job_secondary_skills")
    experience = models.CharField(max_length=50)
    job_description = models.TextField()
