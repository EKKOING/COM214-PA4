from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about-me.html'


class PortfolioPageView(TemplateView):
    template_name = 'projects.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class SocialsPageView(TemplateView):
    template_name = 'socials.html'


class BootstraplessPageView(TemplateView):
    template_name = 'no-bootstrap.html'
