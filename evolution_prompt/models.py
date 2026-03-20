from django.db import models
from django.conf import settings
from constants.hero import Hero
from constants.warrior import Warrior
from constants.wizard import Wizard
from constants.priest import Priest


cclass Character(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    job = models.CharField(max_length=255)
    level = models.IntegerField()
    evolution = models.CharField(max_length=255)

    character_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url =models.ImageField(upload_to='characters/', blank=True)
    create_character = models.DateTimeField()