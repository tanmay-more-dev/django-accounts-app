from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class LoginView(LoginView):
    """Logs User In. Extends Django's default LoginView
    from django.contrib.auth.views"""
    template_name = 'accounts/login.html'
    next_page = reverse_lazy("accounts:success")


class LogoutView(LogoutView):
    """Logs User Out. Extends Django's default LogoutView
    from django.contrib.auth.views"""
    next_page = reverse_lazy("accounts:login")


class SuccessView(LoginRequiredMixin, TemplateView):
    """Handles successful user login."""
    login_url = reverse_lazy("accounts:login")
    template_name = "accounts/after_page.html"
