from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'funcionarios/',
        views.ListaFuncionarios.as_view(),
        name='funcionarios'
    ),
]
