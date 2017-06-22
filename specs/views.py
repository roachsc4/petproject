from specs.models import SpecType, Spec
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect

from specs.models import Lesson
from specs.forms import LessonCreateForm


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


class LessonListView(ListView):
    model = Lesson
    template_name = 'specs/lessons.html'

    def get_context_data(self, **kwargs):
        context = super(LessonListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonCreateForm
    template_name = 'specs/create_lesson.html'
    success_url = reverse_lazy('specs:lessons')


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonCreateForm
    template_name = 'specs/create_lesson.html'
    success_url = reverse_lazy('specs:lessons')

    def get_object(self, *args, **kwargs):
        lesson = get_object_or_404(Lesson, pk=self.kwargs['pk'])
        return lesson

    #def get(self, request, pk):
        #return redirect(reverse_lazy('specs:lessons'))


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class LessonDeleteView(DeleteView):
    model = Lesson
    success_url = reverse_lazy('specs:lessons')

    def get(self, request, pk):
        return redirect(reverse_lazy('specs:lessons'))
