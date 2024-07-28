from django.shortcuts import render
from django.template import Template
from django.views.generic import ListView, TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'