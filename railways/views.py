from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'railways/index.html'


class Register(TemplateView):
    template_name = 'railways/register.html'


