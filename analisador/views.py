import json
from django.shortcuts import render
from .AI import base
from django.core.files.storage import FileSystemStorage
# Create your views here.

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AnaliseGraficoPageView(TemplateView):
    template_name = 'analise-grafico.html'

class UploadArquivoPageView(TemplateView):
    template_name = 'upload-arquivo.html'

def home(request):
    return render(request,'home.html',{})

def grafico(request):
    if request.method == 'POST':
        print("Foioooo")
    #essa função vai receber o arquivo/caminho e vai fazer a chamada da IA, depois do processamento
    #ela vai enviar para a 'analise-grafico.html' dois resultados , o número de frases positivas e negativas
    #os valores podem ser enviados em forma de vetor
    return render(request,'grafico.html',{})

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['arquivo']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        base_caminho = r"C:\Users\juans\OneDrive\Documentos\Webiaus\media'\'"
        base_caminho = base_caminho.replace("'",'')+name 
        contagem = base.analisador_sentimento(base_caminho)
    return render(request,'grafico.html',{
        'contagem': json.dumps(contagem)
    })

