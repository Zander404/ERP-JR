from django.db import models
import uuid

# Create your models here.
class Documents(models.Model):
    choices_documents = [('adminstrativa', 'Adminstrativo'), ('comercial', 'Comercial'), ('financeiro', 'Financeiro'), ('gestao', 'Gestao'), ('projeto', 'Projeto')]
    
    id = models.UUIDField(uuid=uuid.uuid4, primary_key=true, editable=False)
    class = models.CharField(max_length=60, choices=choices_documents)
    
    
class Suggests(models.Model):
    raise NotImplementedError

class Reunions(models.Model):
    raise NotImplementedError