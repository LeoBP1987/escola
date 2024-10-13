from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):

    # Exemplo de um teste qualquer para entender como funciona
    # def teste_falha(self):
    #     self.fail('Teste Falhou!!!!')

    def setUp(self):

        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo Estudante',
            email = 'testemodeloestudante@teste.com',
            cpf = '05623643078',
            data_nascimento = '2024-10-11',
            celular = '99 99999-9999'
        )

    def test_verifica_atributos_de_estudante(self):
        '''Teste que verifica os atributos do modelo Estudante'''

        self.assertEqual(self.estudante.nome, 'Teste de Modelo Estudante')
        self.assertEqual(self.estudante.email, 'testemodeloestudante@teste.com')
        self.assertEqual(self.estudante.cpf, '05623643078')
        self.assertEqual(self.estudante.data_nascimento, '2024-10-11')
        self.assertEqual(self.estudante.celular, '99 99999-9999')

class ModelCursoTestCase(TestCase):

    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'XX01',
            descricao = 'Curso de Teste para verificação de modelo',
            nivel = 'A'
        )

    def test_verifica_atributos_do_curso(self):
        '''Teste que verifica os atributos do modelo Curso'''

        self.assertEqual(self.curso.codigo, 'XX01')
        self.assertEqual(self.curso.descricao, 'Curso de Teste para verificação de modelo')
        self.assertEqual(self.curso.nivel, 'A')

class ModelMatriculaTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):

        self.estudante = Estudante.objects.get(id=94)
        self.curso = Curso.objects.get(id=16)

        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'N'
        )

    def test_verifica_atributos_da_matricula(self):
        '''Teste que verifica os atributos do modelo Matricula'''

        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.periodo, 'N')