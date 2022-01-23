from dataclasses import fields
from rest_framework import serializers
from .models import *
class gradeserializer(serializers.ModelSerializer):
     class Meta:
         model=grades
         fields='__all__'