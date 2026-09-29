from django.urls import path
from . import views
from .views import MinhaCBV

app_name = 'website' # Essencial para bater com o namespace='website'

urlpatterns = [
    # Manter aqui as suas rotas anteriores (exemplo: caminho para index ou lista_funcionarios)
    path('', views.index, name='index'),
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    
    # Rotas novas para a Atividade 5
    path('fbv/', views.minha_fbv, name='minha_fbv'),
    path('cbv/', MinhaCBV.as_view(), name='minha_cbv'),
]