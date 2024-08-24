from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'  # Update to match the correct path

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'  # Update to match the correct path
