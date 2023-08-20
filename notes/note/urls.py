from django.urls import path
from .views import add_note, details_note, edit_note, delete_note


urlpatterns = [
    path('add/', add_note, name='add-note'),
    path('details/<int:note_id>', details_note, name='note-details'),
    path('edit/<int:note_id>', edit_note, name='edit-note'),
    path('delete/<int:note_id>', delete_note, name='delete-note'),
]