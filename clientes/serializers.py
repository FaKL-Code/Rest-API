from xml.dom import ValidationErr
from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("CPF invalido")
        return cpf
    
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Nome não aceita caracteres numéricos")
        return nome
    
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("RG invalido")
        return rg
    
    def validate_celular(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError("Celular invalido")
        return celular
    