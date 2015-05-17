from django.db import models

# Create your models here.

# Class definition for a Personal Project.
class Project(models.Model):
    PROJECT_TYPE = {
        "Design": 1,
        "Software": 2,
        "Build": 3,
    }

    PROJECT_CHOICES = (
        (1, "Design"),
        (2, "Software"),
        (3, "Build"),
        (4, "Other"),
    )


    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=3000)
    type = models.IntegerField(choices=PROJECT_CHOICES)

# Class definition for a File for a personal project
class ProjectFile(models.Model):
    file = models.FileField(upload_to="project_files")              # File
    project = models.ForeignKey(Project)                            # Project file is associated with