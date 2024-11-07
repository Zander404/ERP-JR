from django.db import models
import uuid

# Create your models here.
class AutorizacaoGasto(models.Model):
    id = models.UUIDField(uuid=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=144)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_by = models.ManyToManyField