from specs.models import SpecType, Spec
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist

from specs.models import Lesson, TraineeLesson, Test, TraineeTest, Question, Answer
from specs.forms import LessonCreateForm, TestCreateForm, QuestionCreateForm, AnswerCreateForm


class SpecTypeCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')

    model = SpecType
    fields = ['name']
    template_name = 'specs/create_spec_type.html'
    success_url = reverse_lazy('vacancies:vacancies')


class SpecCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')

    model = Spec
    fields = ['name', 'type']
    template_name = 'specs/create_spec.html'
    success_url = reverse_lazy('vacancies:vacancies')


class LessonListView(ListView):
    model = Lesson
    template_name = 'specs/lessons.html'


class LessonDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')

    model = Lesson
    template_name = 'specs/lesson_detail.html'

    def get_object(self, *args, **kwargs):
        lesson = get_object_or_404(Lesson, pk=self.kwargs['pk'])
        return lesson

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        lesson = context['object']
        try:
            if TraineeLesson.objects.get(trainee=self.request.user, lesson=lesson):
                context['is_finished'] = True
        except ObjectDoesNotExist:
            context['is_finished'] = False
        return context


class LessonCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')

    model = Lesson
    form_class = LessonCreateForm
    template_name = 'specs/create_lesson.html'
    success_url = reverse_lazy('specs:lessons')


class LessonUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')

    model = Lesson
    form_class = LessonCreateForm
    template_name = 'specs/create_lesson.html'
    success_url = reverse_lazy('specs:lessons')

    def get_object(self, *args, **kwargs):
        lesson = get_object_or_404(Lesson, pk=self.kwargs['pk'])
        return lesson


class LessonDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')

    model = Lesson
    success_url = reverse_lazy('specs:lessons')

    def get(self, request, pk):
        raise NotImplemented


class LessonPassView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, pk):
        raise NotImplemented

    def post(self, request, pk):
        lesson = Lesson.objects.get(pk=pk)
        user = request.user
        trainee_lesson = TraineeLesson(trainee=user, lesson=lesson, status=2)
        trainee_lesson.save()

        return redirect(request.META.get('HTTP_REFERER'))


class TestCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')

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


class TestListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')

    model = Test
    template_name = 'specs/tests.html'


class TestDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')

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


class TestUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')

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


class TestDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')

    model = Lesson
    success_url = reverse_lazy('specs:tests')

    def get(self, request, pk):
        raise NotImplemented


class TestSetView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users:login')

    template_name = 'specs/test_set.html'

    def get_context_data(self, **kwargs):
        context = super(TestSetView, self).get_context_data(**kwargs)
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        questions = Question.objects.filter(test=test)
        context['test'] = test
        context['questions'] = questions
        return context


class QuestionCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')

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


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')

    model = Question
    form_class = QuestionCreateForm
    template_name = 'specs/create_test.html'

    def get_object(self, *args, **kwargs):
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        return question

    def get_success_url(self):
        test = get_object_or_404(Question, pk=self.kwargs['pk']).test
        return reverse_lazy('specs:set_test', kwargs={'pk': test.pk})


class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')

    model = Question

    def get(self, request, pk):
        raise NotImplemented

    def get_success_url(self):
        test = get_object_or_404(Question, pk=self.kwargs['pk']).test
        return reverse_lazy('specs:set_test', kwargs={'pk': test.pk})


class QuestionSetView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users:login')

    template_name = 'specs/question_set.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionSetView, self).get_context_data(**kwargs)
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        answers = Answer.objects.filter(question=question)
        context['question'] = question
        context['answers'] = answers
        return context


class AnswerCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')

    model = Answer
    form_class = AnswerCreateForm
    template_name = 'specs/create_answer.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.question = get_object_or_404(Question, pk=self.kwargs['pk'])
        return super(AnswerCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('specs:set_question', kwargs={'pk': self.kwargs['pk']})


class AnswerUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')

    model = Answer
    form_class = AnswerCreateForm
    template_name = 'specs/create_answer.html'

    def get_object(self, *args, **kwargs):
        answer = get_object_or_404(Answer, pk=self.kwargs['pk'])
        return answer

    def get_success_url(self):
        question = get_object_or_404(Answer, pk=self.kwargs['pk']).question
        return reverse_lazy('specs:set_question', kwargs={'pk': question.pk})


class AnswerDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')

    model = Answer

    def get(self, request, pk):
        raise NotImplemented

    def get_success_url(self):
        question = get_object_or_404(Answer, pk=self.kwargs['pk']).question
        return reverse_lazy('specs:set_question', kwargs={'pk': question.pk})
