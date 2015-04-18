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
    file = models.FileField(upload_to="project_files")
    project = models.ForeignKey(Project)

# Class definition for a personal blog
class Blog(models.Model):
    title = models.CharField(max_length=100)                       # Blog Positing Title
    summary = models.TextField(max_length=5000)                    # Summary text of blog post
    image = models.ImageField(upload_to="blog_images", blank=True) # Image for Blog Posting
    project = models.ForeignKey(Project, blank=True, null=True)    # Specify a project this blog posting belongs to

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
