from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class PageNotFoundView(TemplateView):
    template_name = '404.html'

class AboutUsView(TemplateView):
    template_name = 'about-us.html'
