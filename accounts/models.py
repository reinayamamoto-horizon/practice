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
    character = models.ForeignKey(
        "Character",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    display_flag = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_flag = models.BooleanField(default=False)

class Character(models.Model):  # 初期未設定OK
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="character")
    job = models.ForeignKey("Job", on_delete=models.SET_NULL, null=True, blank=True) 
    level = models.IntegerField(default=1) 
    exp = models.IntegerField(default=0) 
    evolution = models.CharField(max_length=255, blank=True, default="")
    character_name = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(
        upload_to="characters/",
        blank=True,
        default="characters/initial_female.png",
    )
    
class Job(models.Model):
    job_id = models.CharField(max_length=255)
    stage = models.IntegerField()
    class Meta:
        unique_together = ("job_id", "stage")


