from django.db import models
from django.core.validators import MinLengthValidator

class Estudante(models.Model):

    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank=False)
    cpf = models.CharField(max_length = 11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome


class Curso(models.Model):

    NIVEIS = [
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado')
    ]

    codigo = models.CharField(max_length = 10, unique=True, validators=[MinLengthValidator(3)])
    descricao = models.CharField(max_length = 100, null=False)
    nivel = models.CharField(max_length = 1, choices=NIVEIS, null=False, blank=False, default='B')

    def __str__(self):
        return self.codigo
    
class Matricula(models.Model):

    PERIODO = [
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    ]

    estudante = models.ForeignKey(
        to=Estudante,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )

    curso = models.ForeignKey(
        to=Curso,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )

    periodo = models.CharField(max_length=1, choices=PERIODO, null=False, blank=False, default='M')





