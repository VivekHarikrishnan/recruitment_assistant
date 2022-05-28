from django.db import models
from django.utils.translation import gettext_lazy as _
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
        return f"{self.name} ({self.country.name})"


class Job(models.Model):
    class Status(models.TextChoices):
        OPEN = 'OPEN', _('Open')
        CLOSED = 'CLOSED', _('Closed')
        FULLFILlED = 'FULLFILlED', _('Fullfilled')
        CANCELLED = 'CANCELLED', _('Cancelled')
        DRAFT = 'DRAFT', _('Draft')

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Developer")
    primary_skills = models.ManyToManyField(Skill, related_name="job_primary_skills")
    secondary_skills = models.ManyToManyField(Skill, related_name="job_secondary_skills")
    experience = models.CharField(max_length=50)
    job_description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)

    def __str__(self) -> str:
        return f"{self.company.name} - {self.title}"
