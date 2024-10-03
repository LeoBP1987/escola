from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, \
    ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EstudanteViewSet(viewsets.ModelViewSet):
    '''
    Este viewset fornece operações CRUD para o modelo Estudante.

    Funções:
    - Obtem todos os estudantes cadastrados, ordenados pelo ID.
    - Suporta busca nos campos 'nome' e 'cpf'.
    - Ordenação disponível pelo campo 'nome'.
    
    Detalhes:
    - Emprega diferentes serializadores baseados na versão da API:
      - Utiliza EstudanteSerializerV2 para a versão 'v2'
      - Utiliza EstudanteSerializer para outras versões
    - Aplica limite de requisições para usuarios anônimos e logados (aplicado globalmente pelo settings).
    - Exige autenticação de usuarios e aplica as permissões atribuidas via Admin (aplicado globalmente pelo settings).
    '''
    queryset = Estudante.objects.all().order_by('id')
    #serializer_class = EstudanteSerializer essa é a linha que deve ser definida para trabalhar quando a apenas uma versão da API
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome',]
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    '''
    Esta viewset fornece operações CRUD para o modelo Curso

    Funções:
    - Obtem todos os estudantes cadastrados, ordenados pelo ID.

    Detalhes:
    - Aplica limite de requisições para usuarios anônimos e logados (aplicado globalmente pelo settings).
    - Exige autenticação de usuarios e aplica as permissões atribuidas via Admin (aplicado globalmente pelo settings).
    '''
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class MatriculaViewSet(viewsets.ModelViewSet):
    '''
    Esta viewset fornece operações CRUD para o modelo Matricula

    Funções:
    - Obtem todos as matriculas cadastradas, ordenadas pelo ID.

    Detalhes:
    - Aplica limite de requisições para usuarios anônimos e logados localmente, com um classe especifica para requisições anônimas (MatriculaAnonRateThrottle).
    - Exige autenticação de usuarios e aplica as permissões atribuidas via Admin (aplicado globalmente pelo settings).
    - Só permite requisições de metodo 'get' e 'post' via API.
    '''
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]

class ListaMatriculaEstudante(generics.ListAPIView):
    '''
    Exibe matriculas por estudante.

    Parâmetros:
    id: int
        - Chave primária que identifica o estudante cuja as matriculas devem ser consultadas.
    '''
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['id']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    '''
    Exibe matriculas por curso.

    Parâmetros:
    id: int
        - Chave primária que identifica o curso cujo as matriculas devem ser consultadas.
    '''

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['id']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer