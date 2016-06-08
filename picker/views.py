from django import forms
from forms import UserCreationFormEmail
from django.http import HttpResponseRedirect
from django.shortcuts import render



def register(request):
    if request.method == 'POST':
        form = UserCreationFormEmail(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
