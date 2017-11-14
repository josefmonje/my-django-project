from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class RobotsTxtView(generic.TemplateView):
    template_name = 'robots.txt'
