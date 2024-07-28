from django.contrib import admin
from .models import Introducao, ImagemIntroducao, RedesSociais, CV, SobreMim, ImagemSobreMim, Experiencias, Habilidades, Projetos, Contato

class IntroducaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'descricao')
    fieldsets = ()


class ImagemIntroducaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagem', 'alt')
    list_display_links = ('id', 'imagem')
    search_fields = ('imagem', 'alt')
    fieldsets = ()


class RedesSociaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'icone', 'url')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'icone', 'url')
    fieldsets = ()


class CVAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'arquivo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'descricao', 'arquivo')
    fieldsets = ()


class SobreMimAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'descricao')
    fieldsets = ()


class ImagemSobreMimAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagem', 'alt')
    list_display_links = ('id', 'imagem')
    search_fields = ('imagem', 'alt')
    fieldsets = ()


class ExperienciasAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa', 'cargo', 'data_inicio', 'data_fim',)
    list_display_links = ('id', 'empresa')
    search_fields = ('empresa', 'cargo', 'data_inicio', 'data_fim', 'stack')
    fieldsets = ()


class HabilidadesAdmin(admin.ModelAdmin):
    list_display = ('id', 'habilidade', 'icone', )
    list_display_links = ('id', 'habilidade')
    search_fields = ('nome', 'icone', 'habilidade')
    fieldsets = ()


class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao',)
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'descricao')
    fieldsets = ()


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'assunto',)
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'email', 'assunto', 'mensagem')
    fieldsets = ()

admin.site.register(Introducao, IntroducaoAdmin)
admin.site.register(ImagemIntroducao, ImagemIntroducaoAdmin)
admin.site.register(RedesSociais, RedesSociaisAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(SobreMim, SobreMimAdmin)
admin.site.register(ImagemSobreMim, ImagemSobreMimAdmin)
admin.site.register(Experiencias, ExperienciasAdmin)
admin.site.register(Habilidades, HabilidadesAdmin)
admin.site.register(Projetos, ProjetosAdmin)
admin.site.register(Contato, ContatoAdmin)
