from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.http import FileResponse, Http404
from apps.sobre.models import Introducao, ImagemIntroducao, RedesSociais, CV, SobreMim, ImagemSobreMim, Experiencias, Habilidades, Projetos, Contato
from apps.sobre.forms import ContatoForm

def index(request):       
    introducao = Introducao.objects.first()
    imagem_introducao = ImagemIntroducao.objects.first()
    redes_sociais = RedesSociais.objects.all().order_by('-id')
    cv = CV.objects.first()
    sobre_mim = SobreMim.objects.first()
    imagem_sobre_mim = ImagemSobreMim.objects.first()
    experiencias = Experiencias.objects.all().order_by('-data_inicio')
    habilidades = Habilidades.objects.all().order_by('id').exclude(habilidade__in=["CSS", "Javascript"])
    projetos = Projetos.objects.all().order_by('-id')
    contato = Contato.objects.first()
    
    if request.method == 'GET':
        form = ContatoForm()
        return render(request, 'index.html', locals())
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            send_mail(
                f'{nome} - {telefone} - {assunto} - {email}', 
                mensagem,
                email,
                ['juliocsoaresa1@gmail.com', ]
            )
            form = ContatoForm()
            messages.info(request, 'Mensagem enviada com sucesso!')
            return render(request, 'index.html', locals())
        else:
            messages.info(request, 'Erro ao enviar mensagem')
    return render(request, 'index.html', locals())


def download_cv(request, cv_id):
    try:
        cv = CV.objects.get(id=cv_id)
        file_path = cv.arquivo.path  # Use .path para obter o caminho do arquivo no sistema de arquivos
    except CV.DoesNotExist:
        raise Http404("Arquivo não encontrado")

    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=cv.arquivo.name)
    return response
