from django.urls import path

from .views import ContatoView

urlpatterns = [
    path('contato/', ContatoView.as_view(), name='contato'),
    # path('sucesso/', ContatoView.as_view(), name='contato_sucesso'),
    # path('erro/', ContatoView.as_view(), name='contato_erro'),
    # path('sucesso/<str:mensagem>/', ContatoView.as_view(), name='contato_sucesso_mensagem'),
]