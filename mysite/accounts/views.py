from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# @login_required


@login_required
def home(request):
    args = {'user': request.user}
    return render(request, 'accounts/home.html', args)
