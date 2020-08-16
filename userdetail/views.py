from django.shortcuts import render, redirect
from .forms import UserResgisterForm



def user_register(request):
    form = UserResgisterForm()
    if request.method == 'POST':
        form = UserResgisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form, 'title':'Register'}
    return render(request, 'userdetail/register.html', context)