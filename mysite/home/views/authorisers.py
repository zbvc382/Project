from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..models import Requester, Request, Authoriser
from ..decorators import authoriser_required


User = get_user_model()


@method_decorator([login_required, authoriser_required], name='dispatch')
class AuthoriserHomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        pending_requests = []

        authoriser_object = Authoriser.objects.filter(user=user)
        requester_objects = Requester.objects.filter(assigned_authoriser=authoriser_object)

        for requester in requester_objects:
            pending_requests += Request.objects.filter(user=requester.user)

        context = {'pending_requests': pending_requests}

        return context
