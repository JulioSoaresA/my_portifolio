from django.db import models

class Introducao(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=100)
    descricao = models.TextField(verbose_name="Descrição")
    
    class Meta:
        verbose_name = 'Introdução'
        verbose_name_plural = 'Introdução'
        db_table = 'introducao'

    def __str__(self):
        return self.titulo


class ImagemIntroducao(models.Model):
    imagem = models.ImageField(verbose_name="Imagem", upload_to='core/static/introducao')
    alt = models.CharField(verbose_name="Texto alternativo", max_length=100)
    
    class Meta:
        verbose_name = 'Imagem de introdução'
        verbose_name_plural = 'Imagens de introdução'
        db_table = 'imagem_introducao'

    def __str__(self):
        return self.alt


class RedesSociais(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100)
    icone = models.CharField(verbose_name="Ícone", max_length=100)
    url = models.URLField(verbose_name="URL")
    
    class Meta:
        verbose_name = 'Rede social'
        verbose_name_plural = 'Redes sociais'
        db_table = 'redes_sociais'

    def __str__(self):
        return self.nome


class CV(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=100)
    descricao = models.TextField(verbose_name="Descrição")
    arquivo = models.FileField(verbose_name="Arquivo", upload_to='core/static/cv')
    
    class Meta:
        verbose_name = 'Curriculum Vitae'
        verbose_name_plural = 'Curriculum Vitae'
        db_table = 'cv'

    def __str__(self):
        return self.titulo


class SobreMim(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=100)
    descricao = models.TextField(verbose_name="Descrição")
    
    class Meta:
        verbose_name = 'Sobre mim'
        verbose_name_plural = 'Sobre mim'
        db_table = 'sobre_mim'

    def __str__(self):
        return self.titulo


class ImagemSobreMim(models.Model):
    imagem = models.ImageField(verbose_name="Imagem", upload_to='core/static/sobre')
    alt = models.CharField(verbose_name="Texto alternativo", max_length=100)
    
    class Meta:
        verbose_name = 'Imagem sobre mim'
        verbose_name_plural = 'Imagens sobre mim'
        db_table = 'imagem_sobre_mim'

    def __str__(self):
        return self.alt


class Experiencias(models.Model):
    empresa = models.CharField(verbose_name="Empresa", max_length=100)
    logo = models.ImageField(verbose_name="Logo", upload_to='core/static/experiencias')
    cargo = models.CharField(verbose_name="Cargo", max_length=100)
    data_inicio = models.DateField(verbose_name="Data de início")
    data_fim = models.DateField(verbose_name="Data de fim", blank=True, null=True)
    stack = models.TextField(verbose_name="Stack")
    
    class Meta:
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiências'
        db_table = 'experiencias'

    def __str__(self):
        return self.empresa


class Habilidades(models.Model):
    habilidade = models.CharField(verbose_name="Habilidade", max_length=100)
    icone = models.CharField(verbose_name="Ícone", max_length=100)
    
    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'
        db_table = 'habilidades'

    def __str__(self):
        return self.habilidade


class Projetos(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=100)
    descricao = models.TextField(verbose_name="Descrição")
    imagem = models.ImageField(verbose_name="Imagem", upload_to='core/static/projetos')
    alt = models.CharField(verbose_name="Texto alternativo", max_length=100)
    stack = models.ManyToManyField(Habilidades, verbose_name="Stack", related_name='projetos')
    repo = models.URLField(verbose_name="Repositório")
    site = models.URLField(verbose_name="Site", blank=True, null=True)
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        db_table = 'projetos'

    def __str__(self):
        return self.titulo


class Contato(models.Model):
    assunto = models.CharField(verbose_name="Assunto", max_length=100)
    nome = models.CharField(verbose_name="Nome", max_length=100)
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(verbose_name="Telefone", max_length=19)
    mensagem = models.TextField(verbose_name="Mensagem")
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        db_table = 'contato'
    
    def __str__(self):
        return self.nome
