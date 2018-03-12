from django.contrib import messages
from django.views.generic import TemplateView, UpdateView, FormView, View
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from datetime import datetime
import pytz
from ..forms import EmailForm, RestricionForm, Restriction
from ..models import Requester, Request, Authoriser, Event
from ..decorators import authoriser_required

User = get_user_model()


@method_decorator([login_required, authoriser_required], name='dispatch')
class AuthoriserHomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        authoriser_requests = []
        pending_requests_only = []

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
    template_name = 'Authoriser/update.html'
    success_message = 'Absence request status updated'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        request_object = self.get_object()
        decision = form.cleaned_data['status']
        comment = form.cleaned_data['comment']
        link = 'rhul.herokuapp.com' + reverse('home:check', args=(request_object.id,))

        if decision == 'Approved':
            event = Event(user=request_object.user,
                          title=request_object.get_leave_type(),
                          description='Approved on: ' + request_object.get_updated_at() + '\n' +
                          'Comment: ' + comment,
                          link=link,
                          start=datetime(request_object.start.year, request_object.start.month,
                                         request_object.start.day, tzinfo=pytz.UTC),
                          end=datetime(request_object.end.year, request_object.end.month,
                                       request_object.end.day, tzinfo=pytz.UTC),
                          organizer=request_object.user.username
                          )
            event.save()

        email_subject = 'The decision for Absence Request #' + str(request_object.id) + ' is now available.'
        email_from = 'zbvc382@gmail.com'
        email_to = request_object.user.email

        html_content = loader.render_to_string(
            'Authoriser/update_auto_email_body.html',
            {
                'name': request_object.user.first_name,
                'id': str(request_object.id),
                'link': link,
            }
        )

        email = EmailMultiAlternatives(email_subject, "", email_from, [email_to])
        email.attach_alternative(html_content, "text/html")
        email.send()

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
    template_name = 'Authoriser/contact.html'
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
                'Authoriser/email_body.html',
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
            messages.add_message(self.request, messages.SUCCESS, 'Email sent')

            return super().form_valid(form)

        except ObjectDoesNotExist:

            print('Request object does not exist.')


@method_decorator([login_required, authoriser_required], name='dispatch')
class AuthoriserMyRequestersView(TemplateView):
    template_name = 'Authoriser/my_requesters.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        authoriser_object = Authoriser.objects.filter(user=user)
        requester_objects = Requester.objects.filter(assigned_authoriser=authoriser_object)

        context = {
            'requesters': requester_objects
        }

        return context


@method_decorator([login_required, authoriser_required], name='dispatch')
class AuthoriserCreateRestrictionView(FormView):
    template_name = 'Authoriser/restriction_form.html'
    form_class = RestricionForm

    def get_context_data(self, **kwargs):
        context = super(AuthoriserCreateRestrictionView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        requester = Requester.objects.get(id=pk)
        restrictions = Restriction.objects.filter(user=requester)

        context['requester'] = requester
        context['restrictions'] = restrictions

        return context

    def form_valid(self, form):
        pk = self.kwargs['pk']
        form_user = Requester.objects.get(id=pk)
        o = form.save()
        o.user = form_user
        o.save()
        messages.add_message(self.request, messages.SUCCESS, 'Calendar constraint created')

        return redirect(reverse('home:create_restriction', args=(form_user.id,)))


@method_decorator([login_required, authoriser_required], name='dispatch')
class AuthoriserRemoveRestriction(SuccessMessageMixin, View):
    model = Restriction

    def delete_restriction(self):
        pk = self.kwargs['pk']
        restriction_object = Restriction.objects.get(id=pk)
        restriction_object.delete()

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        restriction_object = Restriction.objects.get(id=pk)
        requester_object = restriction_object.user
        self.delete_restriction()
        messages.add_message(self.request, messages.ERROR,
                             'Calendar constraint removed')

        return redirect(reverse('home:create_restriction', args=(requester_object.id,)))
