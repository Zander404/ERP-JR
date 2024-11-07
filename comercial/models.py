from django.db import models
from django.core.exceptions import ValidationError
import uuid 
from .utils import validation_cpf, cep_format_validator, cnpj_validation, validation_phone


class ProjectType(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.name
    
    
class Adress(models.Model):
    adress = models.CharField(max_length=150)
    city = models.CharField()
    state = models.CharField()
    country = models.CharField()
    cep = models.CharField(max_length=8, validators=[cep_format_validator])


class Client(models.Model):
    id = models.UUIDField(uuid=uuid.uuid4, editable=False, primary_key=True)
    cpf = models.CharField(max_length=11, validators=[validation_cpf], unique=True)
    rg = models.CharField(max_length=7, validators=[validation_cpf])
    fullname = models.CharField(max_length=250, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=14, validators=[validation_phone]) 
    adress = models.ForeignKey(Adress, related_name='adress', on_delete=models.DO_NOTHING)


class Company(models.Model):
    id = models.UUIDField(uuid=uuid.uuid4, editable=False, primary_key=True)
    cnpj = models.CharField(max_length=14, validators=[cnpj_validation], unique=True)
    name = models.CharField(max_length=250, unique=True)
    fantasy_name = models.CharField(max_length=120)
    address = models.ForeignKey(Adress, related_name='address', on_delete=models.DO_NOTHING)


class Contract(models.Model):
    id = models.UUIDField(uuid=uuid.uuid4, primary_key=True, editable=False)
    project_name = models.CharField(max_length=120, unique=True)
    project_type = models.ForeignKey(ProjectType, related_name='proj_type', on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, related_name='contracts', on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, related_name='contracts', on_delete=models.DO_NOTHING)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    signed_at = models.BooleanField(default=False)


class Proposal(models.Model):
    status_choices = [('wait', 'Esperando Resposta'), ('aproval', 'Aprovado'), ('close', 'Desistiram')]

    id = models.UUIDField(uuid=uuid.uuid4, editable=False, primary_key=True)
    client = models.ForeignKey(Client, related_name='proposals', on_delete=models.DO_NOTHING)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    valid_util = models.DateField()
    status = models.CharField(max_length=30, choices=[status_choices])
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_created=True, auto_now_add=True)
