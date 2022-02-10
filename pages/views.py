from django.views.generic import TemplateView

# OOP --> Object Oriented Programming

class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"