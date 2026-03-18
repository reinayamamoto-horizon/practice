from django.db import models
from django.conf import settings
from constants.hero import Hero
from constants.warrior import Warrior
from constants.wizard import Wizard
from constants.priest import Priest


class Character(models.Model):

    JOB_CHOICES = [
        ("hero", "勇者"),
        ("warrior", "戦士"),
        ("wizard", "魔法使い"),
        ("priest", "僧侶"),
    ]

    EVOLUTION_CHOICES = (
        Hero.CHOICES
        + Warrior.CHOICES
        + Wizard.CHOICES
        + Priest.CHOICES
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="character",
    )
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=50, choices=JOB_CHOICES)
    evolution = models.CharField(
        max_length=50,
        choices=EVOLUTION_CHOICES,
        blank=True,
        default="",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_job_display()})"