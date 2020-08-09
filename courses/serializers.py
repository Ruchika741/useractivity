from rest_framework import serializers
from .models import Activity_Period

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model= Activity_Period
        fields= ('e_id','real_name','tz','activity_periods')