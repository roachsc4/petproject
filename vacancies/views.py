from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from vacancies.models import Vacancy
from vacancies.forms import VacancyCreateForm, VacancyUpdateForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect


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


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class VacancyUpdateView(UpdateView):
    model = Vacancy
    form_class = VacancyUpdateForm
    template_name = 'vacancies/create_vacancy.html'
    success_url = reverse_lazy('vacancies:vacancies')

    def get_object(self, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs['pk'])
        return vacancy

    #def get(self, request, pk):
        #return redirect(reverse_lazy('vacancies:vacancies'))


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class VacancyDeleteView(DeleteView):
    model = Vacancy
    success_url = reverse_lazy('vacancies:vacancies')

    def get(self, request, pk):
        return redirect(reverse_lazy('vacancies:vacancies'))

