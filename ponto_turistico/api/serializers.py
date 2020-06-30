from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from ponto_turistico.models import (
    PontoTuristico, DocIdentificacao
)
from atracoes.models import Atracao
from endereco.models import Endereco
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)  # só passa many se for relacionamento Many to Many
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacoes', 'endereco',
                  'descricao_completa', 'descricao_completa_model',
                  'doc_identificacao'
                  ]
        read_only_fields = ['comentarios', 'avaliacoes']
    '''
         Foi definido um Serializer MethodField, onde o método abaixo é passado como campo 
         de serialização. O retorno do método é considerado um campo com o nome do método
         (sem o get na frente) 
    '''
    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
            ponto.save()

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        endereco = validated_data['endereco']
        doc_identificacao = validated_data['doc_identificacao']
        validated_data.pop('doc_identificacao')
        validated_data.pop('atracoes')
        validated_data.pop('endereco')
        ponto = PontoTuristico.objects.create(
            **validated_data
        )

        self.cria_atracoes(atracoes, ponto)
        end = Endereco.objects.create(**endereco)
        doc = DocIdentificacao.objects.create(**doc_identificacao)

        ponto.endereco = end
        ponto.doc_identificacao = doc
        ponto.save()

        return ponto


    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)



