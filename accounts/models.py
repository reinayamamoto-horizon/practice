from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Prompts(models.Model):
    character = models.ForeignKey(
        "Character",
        on_delete=models.CASCADE
    )
    styles = models.TextField(null=False)
    seed = models.IntegerField(null=False)
    model = models.TextField(null=False)
    negative_prompt = models.TextField(null=False)


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

    character_name = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url =models.ImageField(upload_to='characters/', blank=True)
    create_character = models.DateTimeField()

class Job(models.Model):
    job_id = models.CharField(max_length=255)
    stage = models.IntegerField()
    title = models.CharField(max_length=255)

    class Meta:
        unique_together = ("job_id", "stage")


