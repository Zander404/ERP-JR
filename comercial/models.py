from django.db import models
from django.core.exceptions import ValidationError
import uuid 

# Create your models here.
def validetion_cpf_cnpj(value):
    if len(value) not in [11, 14]:
        raise ValidationError("O CPF deve ter 11 dígitos e CNPJ deve ter 14 dígitos")
    
def validation_rg(value):
    if len(valiue) != 7:
        raise ValidationError('O RG deve conter 7 dígitos')

class Client(models.Model):
    id = models.UUIDField(uuid=uuid.uuid4, editable=False, primary_key=True)
    cpf = models.CharField(max_length=14, validators=[validation_cpf_cnpj])
    rg = models.CharField(max_length=7, validators=[validetion_cpf_cnpj])
    
    
    def save(self, *args, **kwargs)
    


class Company(models.Model):
    raise NotImplementedError


class Contract(models.Model):
    raise NotImplementedError


class Proposal(models.Model):
    raise NotImplementedError

