from django.shortcuts import render
from django.http import FileResponse, Http404
from apps.sobre.models import Introducao, ImagemIntroducao, RedesSociais, CV, SobreMim, ImagemSobreMim, Experiencias, Habilidades, Projetos, Contato


def index(request):
    introducao = Introducao.objects.first()
    imagem_introducao = ImagemIntroducao.objects.first()
    redes_sociais = RedesSociais.objects.all().order_by('-id')
    cv = CV.objects.first()
    sobre_mim = SobreMim.objects.first()
    imagem_sobre_mim = ImagemSobreMim.objects.first()
    experiencias = Experiencias.objects.all().order_by('-data_inicio')
    habilidades = Habilidades.objects.all().order_by('-id')
    projetos = Projetos.objects.all().order_by('-id')
    contato = Contato.objects.first()

    return render(request, 'index.html', locals())


def download_cv(request, cv_id):
    try:
        cv = CV.objects.get(id=cv_id)
        file_path = cv.arquivo.path  # Use .path para obter o caminho do arquivo no sistema de arquivos
    except CV.DoesNotExist:
        raise Http404("Arquivo não encontrado")

    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=cv.arquivo.name)
    return response
