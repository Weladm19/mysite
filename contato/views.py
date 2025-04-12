from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import ContatoForm
from .models import Contato


class ContatoView(CreateView):
    model = Contato 
    template_name = 'contato.html'
    form_class = ContatoForm  
    success_url = '/' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contato'
        return context