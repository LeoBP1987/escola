
import re

'''
Montei a função valida_cpf() apenas por prática, mas a melhor maneira de validar um cpf é através da biblioteca validate-docbr.
Para usa-la, é preciso antes instala-la pelo comando (pip install validate-docbr). Em seguida, é precio importa-la para a página (From validate_docbr import CPF).
O uso na função deve seguir a seguinte estrutura:
        cpf = CPF()
        cpf.validate("012.345.678-90")  # True
        cpf.validate("012.345.678-91")  # False
'''

def valida_cpf(cpf):

        valido = False
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) == 11:
            
            soma = sum(int(cpf[i]) * (10 - i) for i in range(0,9))
            resto = soma % 11
            verificador_1 = 0 if resto < 2 else 11 - resto

            soma_2 = sum(int(cpf[i]) * (11 - i) for i in range(0,10))
            resto_2 = soma_2 % 11
            verificador_2 = 0 if resto_2 <2 else 11 - resto_2

            if (verificador_1 == int(cpf[9])) and (verificador_2 == int(cpf[10])):
                valido = True

        return valido

def cpf_invalido(cpf):
        return not valida_cpf(cpf)

def nome_invalido(nome):
        return not nome.replace(" ", "").isalpha()

def celular_invalido(celular):
        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(modelo, celular)

        return not resposta