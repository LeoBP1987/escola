from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Estudante
from rest_framework import status
from escola.serializers import EstudanteSerializer

class EstudanteTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):

        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(self.usuario)

        self.estudante_01 = Estudante.objects.get(id=94)

        self.estudante_02 = Estudante.objects.get(id=95)

    def test_requisicao_get_lista_estudantes(self):
        '''Teste de requisição GET para lista de estudantes'''

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_lista_um_estudante(self):
        '''Teste de requisição GET para lista de um estudante'''

        response = self.client.get(self.url+'94/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dados_estudante = Estudante.objects.get(id=94)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data

        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_cria_um_estudante(self):
        '''Teste de requisição POST para criação de um estudante'''

        dados = {
            'nome':'Estudante Teste',
            'email':'estudante@teste.com',
            'cpf':'09093028049',
            'data_nascimento':'2024-10-13',
            'celular':'99 99999-9999'
        }

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_um_estudante(self):
        '''Teste de requisição delete para um estudante'''

        response = self.client.delete(f'{self.url}95/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_atualiza_um_estudante(self):
        '''Teste de requisição PUT para atualizar um estudante'''

        dados = {
            'nome':'Estudante Teste PUT',
            'email':'estudanteput@teste.com',
            'cpf':'16336661075',
            'data_nascimento':'2024-12-10',
            'celular':'99 99999-9999'
        }

        response = self.client.put(f'{self.url}94/', data=dados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
