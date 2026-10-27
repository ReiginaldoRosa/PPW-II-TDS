from django.urls import path
from . import views
from .views import MinhaCBV

app_name = 'website' # Essencial para bater com o namespace='website'

urlpatterns = [
    # Manter aqui as suas rotas anteriores (exemplo: caminho para index ou lista_funcionarios)
    path('', views.index, name='index'),

    path(
        'funcionarios/', 
        views.FuncionarioListView.as_view(),
        name='lista_funcionarios'
    ),
    
    path(
        'funcionario/<id>',
        views.FuncionarioUpdateView.as_view(),
        name = 'atualiza_funcionario'
    ),

    path(
        'funcionario/excluir/<pk>',
        views.FuncionarioDeleteView.as_view(),
        name = 'deleta_funcionario'
    ),

    path(
        'funcionario/cadastrar/',
        views.FuncionarioCreateView.as_view(),
        name = 'cadastra_funcionario'
    ),
    # --- ADICIONE ESTAS DUAS ROTAS NOVAS AQUI ---
    path('fbv/', views.minha_fbv, name='minha_fbv'),
    path('cbv/', MinhaCBV.as_view(), name='minha_cbv'),

]