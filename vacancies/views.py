from django.shortcuts import render
from django.views.generic.edit import FormView, UpdateView, CreateView

from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect


from vacancies.models import Vacancy
from vacancies.forms import VacancyCreateForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'

    def get_context_data(self, **kwargs):
        context = super(VacancyListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class VacancyCreateView(CreateView):
    model = Vacancy
    form_class = VacancyCreateForm
    template_name = 'vacancies/create_vacancy.html'
    success_url = reverse_lazy('vacancies:vacancies')

    def get_form_kwargs(self):
        kwargs = super(VacancyCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


