from django import forms
from forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.conf import settings

def main(request):
    if request.user.is_authenticated():
        #user is good
        return render(request, "main.html")
    else:
        #user not authenticated, redirect
        return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", {
        'form': form,
    })



def reset_confirm(request, user=None, token=None):
    return password_reset_confirm(request, template_name='auth/reset/password_reset_confirm.html',
        uidb64=user, token=token, post_reset_redirect=reverse('login'))


def reset(request):
    return password_reset(request, from_email=settings.DEFAULT_FROM_EMAIL, template_name='auth/reset/password_reset_form.html',
        email_template_name='auth/reset/password_reset_email.html',
        subject_template_name='auth/reset/password_reset_subject.txt',
        post_reset_redirect=reverse('login'))

# from django.conf import settings
# from django.contrib.auth.forms import PasswordResetForm
# p = PasswordResetForm()
# u = p.get_users('drew@drewmcdermott.net')
# for user in u:
#   print u.email
# p.send_mail(to_email='drew@drewmcdermott.net', email_template_name='auth/reset/password_reset_email_test.html', subject_template_name='auth/reset/password_reset_subject.txt', context={}, from_email=settings.DEFAULT_FROM_EMAIL)
