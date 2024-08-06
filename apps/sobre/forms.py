from django import forms
from .models import Contato
from django.contrib import messages


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'assunto': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
        
    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        assunto = cleaned_data.get('assunto')
        mensagem = cleaned_data.get('mensagem')
        
        if not nome:
            self.add_error('nome', 'Campo obrigatório')
        if not email:
            self.add_error('email', 'Campo obrigatório')
        if not assunto:
            self.add_error('assunto', 'Campo obrigatório')
        if not mensagem:
            self.add_error('mensagem', 'Campo obrigatório')
