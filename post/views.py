from django.views.generic import TemplateView

class AllPostView(TemplateView):
    template_name = 'home.html'
