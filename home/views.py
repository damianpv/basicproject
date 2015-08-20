from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['header_menu'] = 'home'
        return context


class Test1View(TemplateView):
    template_name = 'test/index1.html'

    def get_context_data(self, **kwargs):
        context = super(Test1View, self).get_context_data(**kwargs)
        context['header_menu'] = 'test'
        return context
