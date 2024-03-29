from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco


class DocIdentificacao(models.Model):
    descricao = models.TextField()


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(
        Atracao)
    comentarios = models.ManyToManyField(
        Comentario)
    avaliacoes = models.ManyToManyField(
        Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True
    )
    foto = models.ImageField(upload_to='pontos_turisticos', blank=True, null=True)
    doc_identificacao = models.OneToOneField(
        DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.nome
    '''
        O decorator abaixo retorna o nome e a descrição
        É passado no serializer como campo
    '''
    @property
    def descricao_completa_model(self):
        return '%s - %s' % (self.nome, self.descricao)
