from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, \
                               ListaMatriculasCursoSerializer, EstudanteSerializerV2

class SerializerEstudanteTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):

        self.estudante = Estudante.objects.get(id=94)

        self.estudante.serializers = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializados_de_estudantes(self):
        '''Teste que verifica quais campos que estão sendo serializados de estudante'''

        dados = self.estudante.serializers.data

        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']))

    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        '''Teste que verifica conteudo dos campos que estão sendo serializados de estudante'''

        dados = self.estudante.serializers.data

        self.assertEqual(dados['nome'], self.estudante.nome)
        self.assertEqual(dados['email'], self.estudante.email)
        self.assertEqual(dados['cpf'], self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'], self.estudante.data_nascimento.isoformat())
        self.assertEqual(dados['celular'], self.estudante.celular)

class SerializerCursoTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):

        self.curso = Curso.objects.get(id=16)

        self.curso.serializer = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializados_do_curso(self):
        '''Teste que verifica quais campos que estão sendo serializados do curso'''

        dados = self.curso.serializer.data

        self.assertEqual(set(dados.keys()), set(['id', 'codigo', 'descricao', 'nivel']))

    def test_verifica_conteudo_dos_campos_serializados_do_curso(self):
        '''Teste que verifica o conteudo dos campos que estão sendo serializados do curso'''

        dados = self.curso.serializer.data

        self.assertEqual(dados['codigo'], self.curso.codigo)
        self.assertEqual(dados['descricao'], self.curso.descricao)
        self.assertEqual(dados['nivel'], self.curso.nivel)

class SerializerMatriculaTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):
        
        self.estudante = Estudante.objects.get(id=94)
        self.curso = Curso.objects.get(id=16)

        self.matricula = Matricula(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'N'
        )

        self.matricula.serializer = MatriculaSerializer(instance=self.matricula)

    def test_verifica_campos_serializados_da_matricula(self):
        '''Teste que verifica quais campos que estão sendo serializados da matricula'''

        dados = self.matricula.serializer.data

        self.assertEqual(set(dados.keys()), set(['id', 'estudante', 'curso', 'periodo']))

    def test_verifica_conteudo_dos_campos_serializados_da_matricula(self):
        '''Teste que verifica o conteudo dos campos que estão sendo serializados da matricula'''

        dados = self.matricula.serializer.data

        self.assertEqual(dados['estudante'], self.matricula.estudante.id)
        self.assertEqual(dados['curso'], self.matricula.curso.id)
        self.assertEqual(dados['periodo'], self.matricula.periodo)

class SerializerListaMatriculasEstudanteTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):

        self.estudante = Estudante.objects.get(id=94)
        self.curso = Curso.objects.get(id=16)

        self.matricula = Matricula(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'Noite'
        )

        self.matricula.serializer = ListaMatriculasEstudanteSerializer(instance=self.matricula)

    def test_verifica_campos_serializados_da_lista_matricula_por_estudante(self):
        '''Teste que verifica quais campos que estão sendo serializados da lista de matriculas por estudante'''

        dados = self.matricula.serializer.data

        self.assertEqual(set(dados.keys()), set(['curso', 'periodo']))

    def test_verifica_conteudo_dos_campos_serializados_da_lista_matricula_por_estudante(self):
        '''Teste que verifica o conteudo dos campos que estão sendo serializados da lista de matriculas por estudante''' 

        dados = self.matricula.serializer.data

        self.assertEqual(dados['curso'], self.matricula.curso.descricao)
        self.assertEqual(dados['periodo'], self.matricula.periodo)

class SerializerListaMatriculasCursoTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):

        self.estudante = Estudante.objects.get(id=94)
        self.curso = Curso.objects.get(id=16)

        self.matricula = Matricula(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'Noite'
        )

        self.matricula.serializer = ListaMatriculasCursoSerializer(instance=self.matricula)

    def test_verifica_campos_serializados_da_lista_matricula_por_curso(self):
        '''Teste que verifica quais campos que estão sendo serializados da lista de matriculas por curso'''

        dados = self.matricula.serializer.data

        self.assertEqual(set(dados.keys()), set(['estudante_nome',]))

    def test_verifica_conteudo_dos_campos_serializados_da_lista_matricula_por_estudante(self):
        '''Teste que verifica o conteudo dos campos que estão sendo serializados da lista de matriculas por curso''' 

        dados = self.matricula.serializer.data

        self.assertEqual(dados['estudante_nome'], self.matricula.estudante.nome)

class SerializerEstudanteV2TestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):

        self.estudante = Estudante.objects.get(id=94)

        self.estudante.serializers = EstudanteSerializerV2(instance=self.estudante)

    def test_verifica_campos_serializados_de_estudantes_versao_2(self):
        '''Teste que verifica quais campos que estão sendo serializados de estudantes na versão 2'''

        dados = self.estudante.serializers.data

        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'email', 'celular',]))

    def test_verifica_conteudo_dos_campos_serializados_de_estudante_versao_2(self):
        '''Teste que verifica conteudo dos campos que estão sendo serializados de estudantes na versão 2'''

        dados = self.estudante.serializers.data

        self.assertEqual(dados['nome'], self.estudante.nome)
        self.assertEqual(dados['email'], self.estudante.email)
        self.assertEqual(dados['celular'], self.estudante.celular)        