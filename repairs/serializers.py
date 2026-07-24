from dataclasses import fields
from rest_framework import serializers
from .models import RepairsRequest


class RepairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairsRequest
        fields = '__all__'
        
    def validate_title(self,value):
        if len(value)<5:
            raise serializers.ValidationError('title most be at least 5 characters')
        return value
        
        