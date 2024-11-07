import re
from django.core.exceptions import ValidationError


def valid_cpf(value):
    cpf = re.sub(r'\D', '', value)
    if len(cpf) != 11:
        raise ValidationError('O CPF deve contér 11 dígitos')

    elif cpf == cpf[0]* 11:
        raise ValidationError('O CPF é inválido')

    soma_dig_1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito_1 = (soma_dig_1*10) % 11
    soma_dig_2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito_2 = (soma_dig_2*10) % 11
    print("Digito 1 ", digito_1)
    print("Digito 2 ", digito_2)

    if cpf[-2:] != f'{digito_1}{digito_2}':
        raise ValidationError('O CPF dígitado é inválido')

    return cpf


def format_cep(value):
    cep = re.sub(r'\D', '', value)
    if len(cep) != 8:
        raise ValidationError('O CEP deve contér 8 dígitos')


def format_cnpj(value):
    cnpj = re.sub(r'\D', '', value)

    if len(cnpj) != 11 or len(cnpj) != 14:
        raise ValidationError('O CNPJ deve contér 14 dígitos')


def format_rg(value):
    rg = re.sub(r'\D', '', value)

    if len(rg) != 7:
        raise ValidationError('O RG deve contér 7 dígitos')


def validation_phone(value):
    phone = re.sub(r'\D', '', value)

    if len(phone) != 11 or len(phone) != 14:
        raise ValidationError('O TELEFONE deve contér 11 dígitos ou 14 dígitos')


def calculate_cpf(cpf):
    raise NotImplementedError
