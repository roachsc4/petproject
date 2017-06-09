from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,UserChangeForm
from django.views.generic.edit import FormView,UpdateView
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy

from .forms import UserCreationForm


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "users/login.html"
    success_url = reverse_lazy('index')

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
