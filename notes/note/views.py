from django.shortcuts import render, redirect
from .models import Note
from .forms import AddNoteForm, EditNoteForm, DeleteNoteForm
# Create your views here.
#add_note, details_note, edit_note, delete_note

def add_note(request):
    form = AddNoteForm()
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'note/note-create.html', context=context)


def details_note(request, note_id):
    note = Note.objects.get(id=note_id)
    context = {
        'note': note
    }

    return render(request, 'note/note-details.html', context=context)


def edit_note(request, note_id):
    note = Note.objects.get(id=note_id)
    form = EditNoteForm(instance=note)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'note/note-edit.html', context=context)

def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    form = DeleteNoteForm(instance=note)
    if request.method == 'POST':
        note.delete()
        return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'note/note-delete.html', context=context)
