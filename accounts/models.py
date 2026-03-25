from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Prompt(models.Model):
    character = models.ForeignKey(
        "Character",
        on_delete=models.CASCADE
    )
    styles = models.TextField()
    seed = models.IntegerField()
    model = models.TextField()
    negative_prompt = models.TextField()
    class Meta:
        unique_together = (("character",),)


class Todo(models.Model):
    RANK_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]

    character = models.ForeignKey(
        "Character",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)
    body = models.TextField()
    rank = models.CharField(max_length=1, choices=RANK_CHOICES, default='C')

    display_flag = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)

    delete_flag = models.BooleanField(default=False)


class Character(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    job = models.ForeignKey("Job", on_delete=models.CASCADE)
    level = models.IntegerField(null=False)
    evolution = models.CharField(max_length=255)
    character_name = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to='characters/', blank=True)

class Job(models.Model):
    job_id = models.CharField(max_length=255)
    stage = models.IntegerField()
    class Meta:
        unique_together = ("job_id", "stage")


