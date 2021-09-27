from django.db import models

# Create your models here.

class Door(models.Model):
    door_id = models.IntegerField()

    token_hex = models.CharField(max_length = 16)

    def __str__(self):
        return f"Door key for door number {door_id}"