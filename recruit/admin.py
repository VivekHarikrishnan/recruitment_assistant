from django.contrib import admin
from . import models

admin.site.register(models.Country)
admin.site.register(models.Skill)
admin.site.register(models.Company)


class JobSkillInline(admin.TabularInline):
    model = models.JobSkill
    extra = 5

class JobSkillAdmin(admin.ModelAdmin):
    inlines = (JobSkillInline, )

admin.site.register(models.Job, JobSkillAdmin)
