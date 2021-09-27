from django.db import models

# Create your models here.

def Door(models.model):
    door_id = models.IntegerField()

    token_hex = models.CharField(max_length = 16)

    def __str__:
        return f"Door key for door number {door_id}"