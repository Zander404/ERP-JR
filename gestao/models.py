from django.db import models
import uuid
from ..comercial.validators import valid_cpf, format_rg
from ..comercial.models import Address


class Cargo(models.Model):
    id = models.UUIDField(uuid=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=120)

    def __str__(self):
        return self.name


# class User(models.Models)


class Member(models.Model):
    # cargo_type = [
    #     ('adm', 'Administrativo'),
    #     ('gp', 'Gestão de Pessoas'),
    #     ('proj', 'Projetos'),
    #     ('fin', 'Financeiro'),
    #     ('pres', 'Presidencia')
    #     ]

    id = models.UUIDField(uuid=uuid.uuid4, editable=False, primary_key=True)

#   Personal Info
    cpf = models.CharField(max_length=11, validators=[valid_cpf])  
    rg = models.CharField(max_length=7, validators=[format_rg])
    rg_dispacher = models.CharField(max_length=30)
    full_name = models.CharField(max_length=120, unique=True)
    birthday = models.DateField()
    address = models.ForeignKey(Address, related_name='address',  on_delete=models.CASCADE)
    profission = models.CharField(max_length=60)
    phone = models.CharField(max_length=13, validators=[])
    personal_email = models.EmailField()

    # Company info
    institutional_email = models.EmailField()
    status = models.BooleanField(choices=[('atv', 'Ativo'), ('desatv', 'Desligado')], default='atv')
    cargo = models.ManyToManyField(Cargo, related_name='usuarios')
