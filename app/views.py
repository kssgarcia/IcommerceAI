from django.shortcuts import render, redirect
from users.forms import RegisterForm
from users.models import User

from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView

class Home(TemplateView):
    template_name = 'app/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Login(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authentificated_user = True

    def get_success_url(self):
        return reverse_lazy('page-home')

class PasswordsChangeView(PasswordChangeView):
    template_name = 'app/passwordchange.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('page-home')

class Register(FormView):
    template_name = 'app/register.html'
    form_class = RegisterForm
    redirect_authentificated_user = True
    success_url = reverse_lazy('page-home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user, 'django.contrib.auth.backends.ModelBackend')
        return super(Register, self).form_valid(form)

    def get(self, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('page-home')
        return super(Register, self).get(*args, **kwargs)
