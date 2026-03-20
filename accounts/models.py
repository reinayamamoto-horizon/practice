from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Prompts(models.Model):
    character_id = models.ForeignKey(
        "Character",
        on_delete=models.CASCADE
    )
    styles = models.TextField()
    seed = models.IntegerField()
    model = models.TextField()
    negative_prompt = models.TextField()


class Todo(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE
    )
    character = models.ForeignKey(
        "Character",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)
    body = models.TextField()

    display_flag = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    delete_flag = models.BooleanField(default=False)

class Character(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    job = models.CharField(max_length=255)
    level = models.IntegerField()
    evolution = models.CharField(max_length=255)

    character_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.TextField()
    create_character = models.DateTimeField()

class Job(models.Model):
    job_id = models.CharField(max_length=255)
    stage = models.IntegerField()
    title = models.CharField(max_length=255)

    class Meta:
        unique_together = ("job_id", "stage")


