from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
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
from django.utils import timezone
# Create your views here.


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'

    def get_context_data(self, **kwargs):
        context = super(VacancyListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class VacancyCreateView(CreateView):
    model = Vacancy
    template_name = 'vacancies/create_vacancy.html'
    fields = ['name', 'type', 'dsc']

