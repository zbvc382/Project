from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RequestForm
from .models import Requests


@login_required
def home(request):

    user = request.user
    entries = Requests.objects.filter(user=request.user)

    return render(request, 'home.html', {'user': user, 'entries': entries})


@login_required
def form_request(request):

    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)

        if form.is_valid():
            o = form.save(commit=False)
            o.user = request.user
            o.save()
            messages.success(request, 'Form submitted successfully!')

            return redirect(reverse('home:home'))

    else:

        form = RequestForm()

    return render(request, 'request.html', {'form': form})
