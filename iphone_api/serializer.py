from rest_framework import serializers
from .models import *


class DashboardSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Iphone_Data
        fields = '__all__'

