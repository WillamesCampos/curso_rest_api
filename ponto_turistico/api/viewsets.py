from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ponto_turistico.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    # A queryset definida em queryset é mais limitada, para consultas mais simples.
    # Para consultas mais elaboradas, melhor sobrescrever o método get_queryset
    #queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao', 'endereco__linha1']
    #lookup_field = 'nome'
    permission_classes = [DjangoModelPermissions, ]
    authentication_classes = [TokenAuthentication, ]

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        '''
            Por causa do Lazy load, o hit no banco de dados só é feito quando realizar 
            contagem, acesso a um único elemento, ...
            Caso não, só vai dar um hit no banco quando for retornar.
    
        '''
        if id:
            queryset = PontoTuristico.objects.filter(id=id)
        if nome:
            queryset = PontoTuristico.objects.filter(nome__iexact=nome)
        if descricao:
            queryset = PontoTuristico.objects.filter(descricao__iexact=descricao)

        return queryset

    @action(methods=['POST'], detail=True)
    def denunciar(self, request, pk=None):
        return Response(request.data)
