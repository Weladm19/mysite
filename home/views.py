from django.utils import timezone
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['current_time'] = timezone.now().strftime("%H:%M")
        return context