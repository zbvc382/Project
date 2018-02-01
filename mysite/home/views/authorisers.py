from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from ..forms import RequestForm
from ..models import Request, Requester
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import authoriser_required

User = get_user_model()


@method_decorator([login_required, authoriser_required], name='dispatch')
class AuthoriserHomeView(TemplateView):

    template_name = 'home.html'