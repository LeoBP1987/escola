from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTests(TestCase):

    fixtures = ['prototipo_banco.json']

    def test_carregamento_fistures(self):
        '''Teste de carregamento da fixtures'''

        estudante = Estudante.objects.get(cpf='78863009473')
        curso = Curso.objects.get(id=16)

        self.assertEqual(estudante.celular, '47 96595-6886')
        self.assertEqual(curso.codigo, 'CPOO1')