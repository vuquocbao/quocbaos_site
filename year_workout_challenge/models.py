from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Class definition for a Workout App User
class WorkoutAppUser(models.Model):
    user = models.OneToOneField(User)

# Class definition for a spread sheet with a specific year for a single user
class SpreadSheet(models.Model):
    year = models.IntegerField(default=None)
    user = models.ForeignKey(WorkoutAppUser)

# Class definition of an activity with daily goals and allows multiple activity for a spreadsheet
class Activity(models.Model):
    name = models.CharField(max_length=100)
    daily_goal = models.IntegerField(default=0)
    unit = models.CharField(max_length=200)
    spread_sheet = models.ForeignKey(SpreadSheet)

# Class definition for a daily record of activity. Allows multiple records for a single activity
class Record(models.Model):
    date = models.DateField(default=None)
    activity = models.ForeignKey(Activity)
    spread_sheet = models.ForeignKey(SpreadSheet)




