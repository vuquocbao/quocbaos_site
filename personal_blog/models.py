from django.db import models
from personal_projects.models import Project
# Create your models here.

# Class definition for a personal blog entry
class BlogEntry(models.Model):
    title = models.CharField(max_length=100)                       # Blog Positing Title
    summary = models.TextField(max_length=5000)                    # Summary text of blog post
    image = models.ImageField(upload_to="blog_images", blank=True) # Image for Blog Posting
    project = models.ForeignKey(Project, blank=True, null=True)    # Specify a project this blog posting belongs to

# Class definition image in blog entries
class BlogEntryImage(models.Model):
    image = models.ImageField(upload_to="blog_images", blank=True)
    blog_entry = models.ForeignKey(BlogEntry)