from django.db import models
from django.contrib.auth.models import User


class ResumeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, default='')
    telegram = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=30, default='')
    skills = models.TextField(default=' ')
    languages = models.TextField(default=' ')
    study = models.TextField(default=' ')
    job_experience = models.TextField(default=' ')

