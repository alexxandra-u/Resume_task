from django.db import models
from django.forms import ModelForm
from .models import ResumeModel


class ResumeForm(ModelForm):
    class Meta:
        model = ResumeModel
        fields = ['name', 'telegram', 'email', 'skills', 'languages', 'study', 'job_experience']
