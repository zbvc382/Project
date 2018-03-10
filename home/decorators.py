from django.shortcuts import redirect


def authoriser_required(function):
    def decorator(request, *args, **kwargs):
        if request.user.is_requester:
            return redirect('home:requester')
        if request.user.is_admin:
            return redirect('home:admin')

        return function(request, *args, **kwargs)

    return decorator


def requester_required(function):
    def decorator(request, *args, **kwargs):
        if request.user.is_authoriser:
            return redirect('home:authoriser')
        if request.user.is_admin:
            return redirect('home:admin')

        return function(request, *args, **kwargs)

    return decorator
