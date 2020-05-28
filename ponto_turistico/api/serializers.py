from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from ponto_turistico.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)  # só passa many se for relacionamento Many to Many
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacoes', 'endereco',
                  'descricao_completa', 'descricao_completa_model'
        ]
    '''
         Foi definido um Serializer MethodField, onde o método abaixo é passado como campo 
         de serialização. O retorno do método é considerado um campo com o nome do método
         (sem o get na frente) 
    '''
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
