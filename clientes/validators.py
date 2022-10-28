import re

from clientes.serializers import *
    
def validate_cpf(cpf):
    return len(cpf) == 11
        
def validate_nome(nome):
    return nome.isalpha()

def validate_rg(rg):
    return len(rg) == 9

def validate_celular(celular):
    """Validar celular"""
    modelo = '[0-9]{2}9[0-9]{4}[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta