from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from . import forms

def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CreateUserForm(request.POST) # forma bus duomenimis uzpildyta is "POST"
        if form.is_valid(): # jeigu forma tvarkingai uzpildyta, save ir useris gauna zinute
            form.save()
            messages.success(request, _("Thank you! You can log in now with your credentials."))
            return redirect("index") # kai useris uzpildis teisingai duomenis puslapis uzsidarys
    else:
        form = forms.CreateUserForm()
    return render(request, 'user_profile/signup.html', {
        'form': form,
    })
