from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.base import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

from users.forms import UserCreationForm, TraineeInfoForm
from users.models import TraineeInfo, User


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "users/login.html"
    success_url = reverse_lazy('vacancies:vacancies')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LogoutView(View):
    def post(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        try:
            context['info'] = TraineeInfo.objects.get(user=self.request.user)
        except ObjectDoesNotExist:
            pass

        return context


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class TraineeInfoCreateView(FormView):
    form_class = TraineeInfoForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('users:profile')

    def get_form_kwargs(self):
        kwargs = super(TraineeInfoCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    #def form_valid(self, form):
        #import ipdb; ipdb.set_trace(context=7)
        #form.save()

        #return super(TraineeInfoCreateView, self).form_valid(form)

    #def form_invalid(self, form):
        #import ipdb;ipdb.set_trace()
        #return super(TraineeInfoCreateView, self).form_invalid(form)

        #import ipdb;
        #ipdb.set_trace()


@method_decorator(login_required(login_url=reverse_lazy('users:login')), name='dispatch')
class TraineeInfoUpdateView(UpdateView):
    model = TraineeInfo
    form_class = TraineeInfoForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, *args, **kwargs):
        trainee_info = get_object_or_404(TraineeInfo, user=self.request.user)
        return trainee_info

    def get_form_kwargs(self):
        kwargs = super(TraineeInfoUpdateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


@login_required(login_url=reverse_lazy('users:login'))
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })
