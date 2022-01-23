from dataclasses import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class gradeserializer(serializers.ModelSerializer):
     class Meta:
         model=grades
         fields='__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']