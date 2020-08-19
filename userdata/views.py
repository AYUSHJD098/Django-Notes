from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def dummy(request):
    return redirect(home, request.user.id)

@login_required
def home(request, pk):
    # notes = note.objects.all()
    user = User.objects.get(id=pk)
    if user.id == request.user.id:
        noten = user.note_set.all()
        context = {
            'title': 'Home',
            'notes': noten
        }
        return render(request, 'userdata/home.html', context)
    else:
        return redirect(home, request.user.id)

@login_required
def create_note(request):
    form = noteForm(request.POST or None, request.FILES or None)
    # user = note.author.id()
    if request.method == 'POST':
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = noteForm()
        messages.success(request, 'Your note has been added successfully!')
        return redirect(home, request.user.id)
        

    context = {
        'title': 'Create Note',
        'form': form
    }
    return render(request, 'userdata/createnote.html', context)

@login_required
def view_note(request, pk):
    notes = note.objects.get(id=pk)
    if notes.author.id == request.user.id :
        if request.method == 'POST':
            notes.delete()
            messages.warning(request, 'Your note has been Deleted successfully!')
            return redirect(home, request.user.id)

        context = {
            'title': 'View Note',
            'notes': notes,
        }
        return render(request, 'userdata/viewnote.html', context)
    else:
        return redirect(home, request.user.id)

@login_required
def update_note(request, pk):
    notes = note.objects.get(id=pk)
    form = noteForm(instance=notes)
    if request.method == 'POST':
        form = noteForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your note has been updated successfully!')
            return redirect('home', request.user.id)

    context = {
        'title': 'Edit Note',
        'form': form,
        'notes': notes
    }
    return render(request, 'userdata/updatenote.html', context)



@login_required
def search_note(request):
    search = request.GET['search']
    notetitle =  note.objects.filter(title__icontains=search)
    notenote =  note.objects.filter(note__icontains=search)
    notes = notetitle.union(notenote)
    context = {
        'title': 'Search Note',
        'notes': notes,
       
    }
    return render(request, 'userdata/search.html', context)
