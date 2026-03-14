from django.db import models

# Create your models here.
class Job(models.Model):
    job = models.CharField(max_length=50)

class Evolution(models.Model):
    job_evolution = models.ForeignKey(Job, on_delete=models.CASCADE)
    stage = models.IntegerField()
    title= models.CharField(max_length=100)