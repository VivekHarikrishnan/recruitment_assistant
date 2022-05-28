from django import template
from recruit.models import JobSkill

register = template.Library()

def skills_to_str(skills: list) -> str:
    return ', '.join([skill.name for skill in skills])

@register.filter(name='primary_skills_str')
def convert_primary_skills_str(skills) -> str:    
    return ', '.join([skill.name for skill in skills.filter(jobskill__category=JobSkill.Category.PRIMARY)])


@register.filter(name='secondary_skills_str')
def convert_secondary_skills_str(skills) -> str:
    return ', '.join([skill.name for skill in skills.filter(jobskill__category=JobSkill.Category.SECONDARY)])
