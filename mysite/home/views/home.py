from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class AdminRedirect(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            return redirect('/admin')

        return super(TemplateView, self).dispatch(request, *args, **kwargs)


def home(request):
    if request.user.is_authenticated:
        if request.user.is_requester:
            return redirect('home:requester')
        if request.user.is_admin:
            return redirect('home:admin')

    return render(request, 'home.html')