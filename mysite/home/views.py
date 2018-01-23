from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views import View
from .forms import RequestForm
from .models import Requests


class HomeView(View):
    home_template = 'home.html'

    def get(self, request):
        user = request.user
        entries = Requests.objects.filter(user=request.user)
        return render(request, self.home_template, {'user': user, 'entries': entries})


class RequestView(View):
    request_template = 'request.html'
    form = RequestForm

    def get(self, request):
        return render(request, self.request_template, {'form': self.form})

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            o = form.save(commit=False)
            o.user = request.user
            o.save()
            messages.success(request, 'Form submitted successfully!')

            return redirect(reverse('home:home'))