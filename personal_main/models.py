from django.db import models

# Create your models here.

# Class definition for a work experience
class Job(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    accomplishments = models.TextField(max_length=2000)

# Class definition for a work related project
class WorkProject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    accomplishments = models.TextField(max_length=2000)
    job = models.ForeignKey(Job)
