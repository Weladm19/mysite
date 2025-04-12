from django import forms
from django.core.exceptions import ValidationError

from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        model = Contato
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control contato_view1', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control contato_view2', 'placeholder': 'E-mail'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control contato_view3', 'placeholder': 'Telefone'}),
            'assunto': forms.TextInput(attrs={'class': 'form-control contato_view4', 'placeholder': 'Assunto'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control contato_view5', 'placeholder': 'Mensagem' , 'rows': 1}),
        }
        
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('O campo de e-mail é obrigatório.')
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValidationError('Insira um endereço de e-mail válido.')
        return email
    
    def clena_assunto(self):
        assunto = self.cleaned_data.get('assunto')
        if not assunto:
            raise ValidationError('O campo de assunto é obrigatório.')
        return assunto