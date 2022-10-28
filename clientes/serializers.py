from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import validate_celular, validate_cpf, validate_nome, validate_rg

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF invalido"})
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome':"Nome não pode ter número"})
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg':"RG invalido"})
        if not validate_celular(data['celular']):
            raise serializers.ValidationError({'celular':"Celular invalido"})
        return data