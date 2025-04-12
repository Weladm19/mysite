from django.views.generic import TemplateView


class Midias(TemplateView):
    template_name = 'redes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Minhas Redes'
        context['description'] = 'Minhas Redes Sociais'
        return context