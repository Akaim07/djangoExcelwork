from ast import MatchSequence
from operator import mod
from django.db import models

class grades(models.Model):
    name=models.CharField(max_length=50)
    maths =models.IntegerField(default=0)
    science =models.IntegerField(default=0)
    english=models.IntegerField(default=0)



