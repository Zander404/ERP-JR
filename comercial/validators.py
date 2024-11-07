import re
from django.core.exceptions import ValidationError


def format_cpf(value):
    cpf = re.sub(r'\D', '', value)
    if len(cpf) != 11:
        raise ValidationError('O CPF deve contér 11 dígitos')
    return cpf


def format_cep(value):
    cep = re.sub(r'\D', '', value)
    if len(cep) != 8:
        raise ValidationError('O CEP deve contér 8 dígitos')

 
def format_cnpj(value):
    cnpj = re.sub(r'\D', '', value)
    if len(cnpj) != 11 or len(cnpj) != 14:
        raise ValidationError('O CNPJ deve contér 14 dígitos')


def validation_phone(value):
    phone = re.sub(r'\D', '', value)
    if len(phone) != 11 or len(phone) != 14:
        raise ValidationError('O TELEFONE deve contér 11 dígitos ou 14 dígitos')


def calculate_cpf(cpf):
    raise NotImplementedError
