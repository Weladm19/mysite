from django.urls import path

from .views import Midias

urlpatterns = [
    path('midias/', Midias.as_view(), name='midias'),
]
