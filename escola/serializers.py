from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'
    
    def validate(self, dados):

        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'Insira um CPF válido.'})

        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras.'})
        
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celualar':'O celular precisa estar no seguinte padrão: xx xxxxx-xxxx'})
        
        return dados

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ('curso', 'periodo')

    def get_periodo(self, obj):
        return obj.get_periodo_display() # Obtém o valor da label na lista 'Periodo' definida como Choices para o Model Estudante
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')

    class Meta:
        model = Matricula
        fields = ('estudante_nome',)

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular',]