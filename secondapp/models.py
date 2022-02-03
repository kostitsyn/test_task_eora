from django.db import models


class Spam(models.Model):
    score1 = models.IntegerField(default=1)
