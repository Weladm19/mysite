from django.views.generic import TemplateView


class SobreView(TemplateView):
    template_name = 'sobre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sobre'
        return context