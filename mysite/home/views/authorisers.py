from django.views.generic import TemplateView, UpdateView
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from ..models import Requester, Request, Authoriser
from ..decorators import authoriser_required
from django.urls import reverse_lazy


User = get_user_model()


@method_decorator([login_required, authoriser_required], name='dispatch')
class AuthoriserHomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        authoriser_requests = []
        pending_requests_only = []

        # TODO: variable name changes
        authoriser_object = Authoriser.objects.filter(user=user)
        requester_objects = Requester.objects.filter(assigned_authoriser=authoriser_object)

        for requester in requester_objects:
            authoriser_requests += Request.objects.filter(user=requester.user)
            pending_requests_only += Request.objects.filter(user=requester.user, status='Pending')

        is_pending = False

        if pending_requests_only.__len__() > 0:
            is_pending = True

        array = ['pdf', 'jpg', 'txt', 'docx']
        context = {'authoriser_requests': authoriser_requests, 'array': array,
                   'is_pending': is_pending,
                   'pending_requests': pending_requests_only.__len__()}

        return context


@method_decorator([login_required, authoriser_required], name='dispatch')
class AuthoriserRequestView(SuccessMessageMixin, UpdateView):
    model = Request
    fields = ['comment', 'status']
    template_name = 'update.html'
    success_message = 'Absence request status updated successfully.'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super(AuthoriserRequestView, self).get_context_data(**kwargs)
        array = ['pdf', 'jpg', 'txt', 'docx']
        request_object = self.get_object()
        attachment = request_object.__str__()
        extension = attachment.split('.').pop()
        context['array'] = array
        context['extension'] = extension

        return context
