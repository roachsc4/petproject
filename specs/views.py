from specs.models import SpecType, Spec
from django.views.generic import View
from django.views.generic.base import TemplateView
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

from specs.models import Lesson, TraineeLesson, Test, TraineeTest, Question
from users.models import User
from specs.forms import LessonCreateForm, TestCreateForm, QuestionCreateForm


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class SpecTypeCreateView(CreateView):
    model = SpecType
    fields = ['name']
    template_name = 'specs/create_spec_type.html'
    success_url = reverse_lazy('vacancies:vacancies')


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
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


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class TestCreateView(CreateView):
    model = Test
    form_class = TestCreateForm
    template_name = 'specs/create_test.html'
    success_url = reverse_lazy('specs:tests')

    def get_form_kwargs(self):
        kwargs = super(TestCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get_initial(self):
        if self.kwargs.get('pk'):
            lesson = get_object_or_404(Lesson, pk=self.kwargs.get('pk'))
            name = lesson.name + ' Test'
            return {'lesson': lesson, 'name': name,}
        else:
            super(TestCreateView, self).get_initial()


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class TestListView(ListView):
    model = Test
    template_name = 'specs/tests.html'

    def get_context_data(self, **kwargs):
        context = super(TestListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class TestDetailView(DetailView):
    model = Test
    template_name = 'specs/test_detail.html'

    def get_object(self, *args, **kwargs):
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        return test

    def get_context_data(self, **kwargs):
        context = super(TestDetailView, self).get_context_data(**kwargs)
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        try:
            tt = TraineeTest.objects.get(trainee=self.request.user, test=test)
            context['test_status'] = tt.status
        except ObjectDoesNotExist:
            pass
        return context


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class TestUpdateView(UpdateView):
    model = Test
    form_class = TestCreateForm
    template_name = 'specs/create_test.html'
    success_url = reverse_lazy('specs:tests')

    def get_object(self, *args, **kwargs):
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        return test

    def get_form_kwargs(self):
        kwargs = super(TestUpdateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class TestDeleteView(DeleteView):
    model = Lesson
    success_url = reverse_lazy('specs:tests')

    def get(self, request, pk):
        return redirect(reverse_lazy('specs:tests'))


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class TestSetView(TemplateView):
    template_name = 'specs/test_set.html'

    def get_context_data(self, **kwargs):
        context = super(TestSetView, self).get_context_data(**kwargs)
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        questions = Question.objects.filter(test=test)
        context['test'] = test
        context['questions'] = questions
        return context


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionCreateForm
    template_name = 'specs/create_question.html'

    def get_initial(self):
        if self.kwargs.get('pk'):
            test = get_object_or_404(Test, pk=self.kwargs.get('pk'))
            return {'test': test,}
        else:
            super(QuestionCreateView, self).get_initial()

    def get_success_url(self):
        return reverse_lazy('specs:set_test', kwargs={'pk': self.kwargs['pk']})


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class QuestionUpdateView(UpdateView):
    model = Question
    form_class = QuestionCreateForm
    template_name = 'specs/create_test.html'

    def get_object(self, *args, **kwargs):
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        return question

    def get_success_url(self):
        test = get_object_or_404(Question, pk=self.kwargs['pk']).test
        return reverse_lazy('specs:set_test', kwargs={'pk': test.pk})


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class QuestionDeleteView(DeleteView):
    model = Question

    def get(self, request, pk):
        return reverse_lazy('specs:set_test', kwargs={'pk': self.kwargs['pk']})

    def get_success_url(self):
        test = get_object_or_404(Question, pk=self.kwargs['pk']).test
        return reverse_lazy('specs:set_test', kwargs={'pk': test.pk})
