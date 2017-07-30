from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from vacancies.models import Vacancy
from vacancies.forms import VacancyCreateForm, VacancyUpdateForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'


class VacancyCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')

    model = Vacancy
    form_class = VacancyCreateForm
    template_name = 'vacancies/create_vacancy.html'
    success_url = reverse_lazy('vacancies:vacancies')

    def get_form_kwargs(self):
        kwargs = super(VacancyCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')

    model = Vacancy
    form_class = VacancyUpdateForm
    template_name = 'vacancies/create_vacancy.html'
    success_url = reverse_lazy('vacancies:vacancies')

    def get_object(self, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs['pk'])
        return vacancy


class VacancyDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')

    model = Vacancy
    success_url = reverse_lazy('vacancies:vacancies')

    def get(self, request, pk):
        raise NotImplemented

