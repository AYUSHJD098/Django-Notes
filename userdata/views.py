from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):

    context = {
        'title': 'Home',
        'notes': note.objects.all()
    }
    return render(request, 'userdata/home.html', context)


def create_note(request):
    form = noteForm()

    if request.method == 'POST':
        form = noteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)

    context = {
        'title': 'Create Note',
        'form': form ,
    }
    return render(request, 'userdata/createnote.html', context)


def view_note(request,pk):
    notes = note.objects.get(id=pk)
    if request.method == 'POST':
        notes.delete()
        return redirect(home)

    context = {
        'title': 'View Note',
         'notes': notes
    }
    return render(request, 'userdata/viewnote.html', context)

def update_note(request,pk):
    notes = note.objects.get(id=pk)
    form = noteForm(instance=notes)
    if request.method == 'POST':	
        form = noteForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            return redirect('/')


        
    context = {
        'title': 'Edit Note',
         'form': form ,
         'notes': notes
    }
    return render(request, 'userdata/updatenote.html', context)