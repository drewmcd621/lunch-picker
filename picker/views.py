from django import forms
from forms import UserCreationFormEmail
from django.http import HttpResponseRedirect
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.shortcuts import render



def register(request):
    if request.method == 'POST':
        form = UserCreationFormEmail(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationFormEmail()
    return render(request, "registration/register.html", {
        'form': form,
    })



def reset_confirm(request, uidb36=None, token=None):
    return password_reset_confirm(request, template_name='registration/reset/password_reset_confirm.html',
        uidb36=uidb36, token=token, post_reset_redirect=reverse('login'))


def reset(request):
    return password_reset(request, template_name='registration/reset/password_reset_form.html',
        email_template_name='registration/reset/password_reset_email.html',
        subject_template_name='registration/reset/password_reset_subject.txt',
        post_reset_redirect=reverse('login'))
