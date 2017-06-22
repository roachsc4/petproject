from django.shortcuts import render
from django.views.generic.edit import CreateView
from specs.models import SpecType, Spec
from django.urls import reverse_lazy


class SpecTypeCreateView(CreateView):
    model = SpecType
    fields = ['name']
    template_name = 'specs/create_spec_type.html'
    success_url = reverse_lazy('vacancies:vacancies')


class SpecCreateView(CreateView):
    model = Spec
    fields = ['name', 'type']
    template_name = 'specs/create_spec.html'
    success_url = reverse_lazy('vacancies:vacancies')
