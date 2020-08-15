from django.shortcuts import render

def home(request):
    context = {
        'title':'Home'
    }
    return render(request, 'userdata/home.html', context)


def create_note(request):
    context = {
        'title':'Create Note'
    }
    return render(request, 'userdata/createnote.html', context)