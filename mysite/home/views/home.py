from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        if request.user.is_requester:
            return redirect('home:requester')

    return render(request, 'home.html')