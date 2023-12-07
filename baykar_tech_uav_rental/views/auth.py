from django.shortcuts import render, redirect
from ..forms.auth import RegistrationForm
from django.contrib.auth import login, logout, authenticate


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('baykar_tech_uav_rental/index.html')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {"form": form})
