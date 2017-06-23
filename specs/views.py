from specs.models import SpecType, Spec
from django.views.generic import View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from specs.models import Lesson, TraineeLesson
from users.models import User
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


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'specs/lesson_detail.html'

    def get_object(self, *args, **kwargs):
        lesson = get_object_or_404(Lesson, pk=self.kwargs['pk'])
        return lesson

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        lesson = get_object_or_404(Lesson, pk=self.kwargs['pk'])
        try:
            if TraineeLesson.objects.get(trainee=self.request.user, lesson=lesson):
                context['is_finished'] = True
        except ObjectDoesNotExist:
            context['is_finished'] = False
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


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class LessonPassView(View):
    def get(self, request, pk):
        return redirect(reverse_lazy('specs:lessons'))

    def post(self, request, pk):
        lesson = Lesson.objects.get(pk=pk)
        user = request.user
        trainee_lesson = TraineeLesson(trainee=user, lesson=lesson, status=2)
        trainee_lesson.save()

        return redirect(request.META.get('HTTP_REFERER'))


