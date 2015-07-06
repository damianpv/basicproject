from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['header_menu'] = 'profile'
        return context
