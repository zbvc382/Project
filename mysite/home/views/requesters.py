from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from ..forms import RequestForm
from ..models import Request, Requester
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import requester_required

User = get_user_model()


@method_decorator([login_required, requester_required], name='dispatch')
class RequesterHomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        entries = Request.objects.filter(user=self.request.user)

        ''' get the current user's linked requester object and parse
        id value from one of its fields
        '''
        authoriser_id = Requester.objects.get(user=user.id).assigned_authoriser

        ''' get user object which matches its primary key with the id supplied
        and parse its full name
        '''
        authoriser_name = User.objects.get(id=authoriser_id).get_full_name()

        context = {'user': user, 'entries': entries, 'authoriser': authoriser_name }

        return context


@method_decorator([login_required, requester_required], name='dispatch')
class RequestView(CreateView):
    template_name = 'request.html'
    form_class = RequestForm
    model = Request

    def form_valid(self, form):
        o = form.save(commit=False)
        o.user = self.request.user
        o.save()
        messages.success(self.request, 'Form submitted successfully!')

        return redirect(reverse('home:home'))

