from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/home.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class PageNotFoundView(TemplateView):
    template_name = 'pages/404.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about-us.html'
