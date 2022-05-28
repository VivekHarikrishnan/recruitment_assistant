from django import template

register = template.Library()

@register.filter(name='skills_to_str')
def convert_skills_list_to_str(skills) -> str:
    return ', '.join([skill.name for skill in skills])
