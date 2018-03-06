from django.views.generic import TemplateView, UpdateView, FormView
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ObjectDoesNotExist
from ..forms import EmailForm
from ..models import Requester, Request, Authoriser
from ..decorators import authoriser_required


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

    def form_valid(self, form):
        request_object = self.get_object()
        email_subject = 'The decision for Absence Request #' + str(request_object.id) + ' is now available.'
        email_body = 'Dear ' + request_object.user.first_name\
                     + ',\n\nThe decision of your absence request application #' + str(request_object.id) + ' is now' \
                       ' available to view online.\n\nTo view your decision please log into the Royal Holloway\'s' \
                       ' Absence Management System.\n\n\n**This is an automatically generated email' \
                       ' – please do not reply to it.**'
        email_from = 'zbvc382@gmail.com'
        email_to = request_object.user.email
        send_mail(email_subject, email_body, email_from, [email_to], fail_silently=False,)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AuthoriserRequestView, self).get_context_data(**kwargs)
        array = ['pdf', 'jpg', 'txt', 'docx']
        request_object = self.get_object()
        attachment = request_object.__str__()
        extension = attachment.split('.').pop()
        context['array'] = array
        context['extension'] = extension

        return context


@method_decorator([login_required, authoriser_required], name='dispatch')
class AuthoriserRequestViewEmail(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = EmailForm
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super(AuthoriserRequestViewEmail, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['pk'] = pk

        return context

    def form_valid(self, form):
        subject, from_email, to_email = form.cleaned_data['subject'], 'zbvc382@gmail.com', form.cleaned_data['email']
        text_content = form.cleaned_data['message']
        pk = self.kwargs['pk']

        try:
            request_object = Request.objects.get(id=pk)

            html_content = loader.render_to_string(
                'email_body.html',
                {
                    'text_content': text_content,
                    'application_number': request_object.id,
                    'leave_type': request_object.leave_type,
                    'start': request_object.start,
                    'end': request_object.end,
                    'reason': request_object.reason,
                    'status': request_object.status,
                    'comment': request_object.comment,
                }
            )

            email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            email.attach_alternative(html_content, "text/html")

            if form.cleaned_data['include_attachment'] is True:
                email.attach_file('media/' + request_object.get_attachment())

            email.send()

            return super().form_valid(form)

        except ObjectDoesNotExist:
            print('Request object does not exist.')
