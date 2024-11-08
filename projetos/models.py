from django.db import models
import uuid

# Create your models here.


class ProjectType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=120)


class Team(models.Model):
    raise NotImplementedError


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    type_project = models.ForeignKey()
    title = models.CharField(max_length=50)  
    description = models.TextField(max_length=120)
    manager = models.ForeignKey()


class BoardKanban(models.Model):
    raise NotImplementedError


class TechnicalSupport(models.Model):
    raise NotImplementedError