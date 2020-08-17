from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


def home(request):

    context = {
        'title': 'Home',
        'notes': note.objects.all()
    }
    return render(request, 'userdata/home.html', context)


def create_note(request):
    form = noteForm(request.POST or None, request.FILES or None)
    # user = note.author.id()
    if request.method == 'POST':
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = noteForm()
        messages.success(request, 'Your note has been added successfully!')
        return redirect(home)
        

    context = {
        'title': 'Create Note',
        'form': form
    }
    return render(request, 'userdata/createnote.html', context)


def view_note(request, pk):
    notes = note.objects.get(id=pk)

    if request.method == 'POST':
        notes.delete()
        messages.warning(request, 'Your note has been Deleted successfully!')
        return redirect(home)

    context = {
        'title': 'View Note',
        'notes': notes,
    }
    return render(request, 'userdata/viewnote.html', context)


def update_note(request, pk):
    notes = note.objects.get(id=pk)
    form = noteForm(instance=notes)
    if request.method == 'POST':
        form = noteForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your note has been updated successfully!')
            return redirect('/')

    context = {
        'title': 'Edit Note',
        'form': form,
        'notes': notes
    }
    return render(request, 'userdata/updatenote.html', context)
