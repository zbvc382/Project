from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import Requests


@login_required
def home(request):
    user = request.user
    name = user.userprofile.full_name.split()[0]
    entries = Requests.objects.filter(user=request.user)

    return render(request, 'home/home.html', {'name': name, 'entries': entries})


@login_required
def form_request(request):
    form = forms.RequestForm()
    print(request.user)

    if request.method == 'POST':
        form = forms.RequestForm(request.POST, request.FILES)

        if form.is_valid():
            o = form.save(commit=False)
            o.user = request.user
            o.save()
            messages.success(request, 'Form submitted successfully!')

            return redirect(reverse('home:home'))

    return render(request, 'home/request.html', {'form': form})
