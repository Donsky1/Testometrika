from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .forms import UserLoginForm, MyUserCreatingForm
from .models import MyUser


class UserLoginView(auth_views.LoginView):
    template_name = 'app_user/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = reverse_lazy('index')


class RegistrationView(generic.CreateView):
    model = MyUser
    template_name = 'app_user/registration.html'
    form_class = MyUserCreatingForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegistrationView, self).get(request, *args, **kwargs)