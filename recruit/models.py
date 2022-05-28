from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=75, unique=True)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.code})"


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    domain = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True)
    aliases = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Company(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Developer")
    primary_skills = models.ManyToManyField(Skill, related_name="job_primary_skills")
    secondary_skills = models.ManyToManyField(Skill, related_name="job_secondary_skills")
    experience = models.CharField(max_length=50)
    job_description = models.TextField()

    def __str__(self) -> str:
        return f"{self.company.name} - {self.title}"
