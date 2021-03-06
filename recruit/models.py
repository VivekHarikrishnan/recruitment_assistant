from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Pic(models.Model):
    path = models.CharField(max_length=400)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()


class Country(models.Model):
    name = models.CharField(max_length=75, unique=True)
    code = models.CharField(max_length=3, unique=True)

    class Meta:
        ordering = ['code']
        verbose_name_plural = "Countries"

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
    logo = GenericRelation(Pic)

    class Meta:
        verbose_name_plural = "Companies"

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
    skills = models.ManyToManyField(Skill, through="JobSkill", related_name="job_skills")
    experience = models.CharField(max_length=50)
    job_description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)

    def __str__(self) -> str:
        return f"{self.company.name} - {self.title}"

class JobSkill(models.Model):
    class Category(models.TextChoices):
        PRIMARY = 'PRIMARY', 'Primary'
        SECONDARY = 'SECONDARY', 'Secondary'

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=Category.choices)
    is_mandatory = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.category