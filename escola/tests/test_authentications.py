from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):

        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin'
        )

        self.url = reverse('Estudantes-list')

    def test_verifica_autenticacao_usuario_com_credenciais_corretas(self):
        '''Teste que verifica autenticação de usuario com credenciais corretas'''

        usuario = authenticate(username='admin', password='admin')

        self.assertTrue((usuario is not None) and (usuario.is_authenticated))

    def test_verifica_autenticacao_usuario_com_username_incorreto(self):
        '''Teste que verifica autenticação de usuario com username incorreto'''

        usuario = authenticate(username='xx', password='admin')

        self.assertFalse((usuario is not None) and (usuario.is_authenticated))

    def test_verifica_autenticacao_usuario_com_senha_incorreta(self):
        '''Teste que verifica autenticação de usuario com senha incorreto'''

        usuario = authenticate(username='admin', password='xx')

        self.assertFalse((usuario is not None) and (usuario.is_authenticated))

    def test_requisicao_get_autorizada(self):
        '''Teste de uma requisição GET autorizada'''

        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_nao_autorizada_sem_autenticacao(self):
        '''Teste de uma requisição GET não autorizada por não haver autenticação de usuário'''

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)