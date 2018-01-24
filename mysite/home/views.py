from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from .forms import RequestForm
from .models import Requests


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        entries = Requests.objects.filter(user=self.request.user)
        context = {'user': user, 'entries': entries}

        return context


class RequestView(CreateView):
    template_name = 'request.html'
    form_class = RequestForm
    model = Requests

    def form_valid(self, form):
        o = form.save(commit=False)
        o.user = self.request.user
        o.save()
        messages.success(self.request, 'Form submitted successfully!')

        return redirect(reverse('home:home'))