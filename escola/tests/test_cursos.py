from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Curso
from rest_framework import status
from escola.serializers import CursoSerializer

class CursoTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):

        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(self.usuario)

        self.curso_01 = Curso.objects.get(id=16)

        self.curso_02 = Curso.objects.get(id=17)

    def test_requisicao_get_lista_cursos(self):
        '''Teste de requisição GET para lista de cursos'''

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_lista_um_curso(self):
        '''Teste de requisição GET para lista de um curso'''

        response = self.client.get(self.url+'16/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dados_curso = Curso.objects.get(id=16)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data

        self.assertEqual(response.data, dados_curso_serializados)

    def test_requisicao_post_cria_um_curso(self):
        '''Teste de requisição POST para criação de um curso'''

        dados = {
            'codigo':'TST10',
            'descricao':'Curso Teste 10',
            'nivel':'I'
        }

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_um_curso(self):
        '''Teste de requisição DELETE para um curso'''

        response = self.client.delete(f'{self.url}17/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_atualiza_um_curso(self):
        '''Teste de requisição PUT para atualizar um curso'''

        dados = {
            'codigo':'TST45',
            'descricao':'Curso Teste 45',
            'nivel':'B'
        }

        responde = self.client.put(f'{self.url}16/', data=dados)

        self.assertEqual(responde.status_code, status.HTTP_200_OK)

        
