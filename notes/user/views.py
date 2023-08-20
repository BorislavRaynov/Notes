from django.shortcuts import render, redirect
from .models import Profile
from .forms import CreateProfileForm
from notes.note.models import Note
# Create your views here.
#home_page, profile_details

def home_page(request):
    form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form
    }
    return render(request, 'user/home-page.html', context=context)


def profile_details(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': notes
    }

    return render(request, 'user/profile.html', context=context)

def delete_profile(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    profile.delete()
    notes.delete()
    return redirect('home-page')