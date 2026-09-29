from django.shortcuts import render
from helloworld.models import Funcionario
from django.views.generic import ListView

# Novas importações necessárias para a Atividade 5
from django.http import HttpResponse
from django.views import View

# ---  CÓDIGO ANTERIOR (PRESERVADO) ---
def index(request):
    return lista_funcionarios(request)

def lista_funcionarios(request):
    # Primeiro, buscamos os funcionários
    funcionarios = Funcionario.objects.all()

    # Incluímos os funcionários no contexto
    contexto = {'funcionarios': funcionarios}

    # Retornamos o template
    return render(request, "website/funcionarios.html", contexto)

class ListaFuncionarios(ListView):
    template_name = "website/funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"

# --- ATIVIDADE 5: REQUISITOS DA FBV E CBV (ADICIONADOS AO FINAL) ---
def minha_fbv(request):
    metodo = request.method
    caminho = request.path
    esquema = request.scheme
    param_get = request.GET.get('nome', 'Nenhum')
    
    html = f"""
    <h1>Atividade 5 - Function Based View (FBV)</h1>
    <p><b>Método HTTP:</b> {metodo}</p>
    <p><b>Caminho (Path):</b> {caminho}</p>
    <p><b>Esquema (Scheme):</b> {esquema}</p>
    <p><b>Parâmetro GET ('nome'):</b> {param_get}</p>
    """
    return HttpResponse(html)

class MinhaCBV(View):
    def get(self, request):
        return HttpResponse("<h1>Atividade 5 - Class Based View (CBV)</h1><p>Requisição GET processada com sucesso via CBV!</p>")