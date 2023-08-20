from django import template
from notes.user.models import Profile


register = template.Library()

@register.simple_tag(name='any-user')
def find_user():
    return Profile.objects.first()
