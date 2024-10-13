from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Matricula, Estudante, Curso
from rest_framework import status

class MatriculaTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):

        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(self.usuario)

        self.estudante_01 = Estudante.objects.get(id=94)
        self.estudante_02 = Estudante.objects.get(id=96)

        self.curso_01 = Curso.objects.get(id=16)
        self.curso_02 = Curso.objects.get(id=18) 

        self.matricula_01 = Matricula.objects.create(
            estudante = self.estudante_02,
            curso = self.curso_01,
            periodo = 'M'
        )

    def test_requisicao_get_lista_matriculas(self):
        '''Teste de requisição GET para lista de matriculas'''

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_cria_uma_matricula(self):
        '''Teste de requisição POST para criação de uma matricula'''

        dados = {
            'id':1,
            'estudante':self.estudante_01.id,
            'curso':self.curso_01.id,
            'periodo':'N'
        }

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_uma_matricula(self):
        '''Teste de requisição DELETE para uma matricula'''

        response = self.client.delete(f'{self.url}4/')

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def teste_requisicao_put_atualiza_uma_matricula(self):
        '''Teste de requisição PUT para atualizar uma matricula'''

        dados = {
            'estudante':self.estudante_01.id,
            'curso':self.curso_01.id,
            'periodo':'M'
        }

        response = self.client.put(f'{self.url}1/', data=dados)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        