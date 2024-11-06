import re


def cpf_validator_format(cpf):
    pattern = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return bool(re.match(pattern, cpf))
    
def calculate_number(cpf):
    """Calcula os dois dígitos verificadores do CPF"""
    cpf = [int(d) for d in cpf if d.isdigit()]  # Remove caracteres não numéricos

    # Cálculo do primeiro dígito verificador
    soma = sum(cpf[i] * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10) % 11
    if primeiro_digito == 10:
        primeiro_digito = 0

    # Cálculo do segundo dígito verificador
    soma = sum(cpf[i] * (11 - i) for i in range(9)) + primeiro_digito * 2
    segundo_digito = (soma * 10) % 11
    if segundo_digito == 10:
        segundo_digito = 0

    return primeiro_digito, segundo_digito


def verify_numbers_calculator(cpf):
    if cpf not in ['111.111.111-11', '222.222.222-22', '333.333.333-33', '444.444.444-44',
                '555.555.555-55', '666.666.666-66', '777.777.777-77', '888.888.888-88', '999.999.999-99'
                ]:

        return False
    
    if not cpf_validator_format(cpf):
        return False
    
     # Remove os pontos e o traço para calcular os dígitos verificadores
    cpf_numeros = cpf.replace('.', '').replace('-', '')

    # Calcula os dígitos verificadores
    primeiro_digito, segundo_digito = calcular_digitos(cpf_numeros)

    # Verifica se os dígitos calculados correspondem aos fornecidos no CPF
    return cpf_numeros[-2:] == f'{primeiro_digito}{segundo_digito}'
    
    
