from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings


# Create your views here.
# @login_required

def home(request):
    args = {'user': request.user}
    return render(request, 'accounts/home.html', args)