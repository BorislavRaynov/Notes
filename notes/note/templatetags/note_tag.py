from django import template
from notes.note.models import Note


register = template.Library()

@register.simple_tag(name='any-notes')
def find_notes():
    return Note.objects.all()
