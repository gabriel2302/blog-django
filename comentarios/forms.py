from django.forms import ModelForm
from .models import Comentarios

class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        if len(nome) < 3:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais de 3 caracteres!'
            )
        if not comentario:
            self.add_error(
                'comentario',
                'Você não realizou um comentário!'
            )
        if len(comentario) <10:
            self.add_error(
                'comentario',
                'Seu comentário é muito curto!'
            )

    class Meta:
        model = Comentarios
        fields = ('nome_comentario', 'email_comentario', 'comentario',)