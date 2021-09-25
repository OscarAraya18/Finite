from rest_framework import serializers
from .models import truthTable

class truthTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = truthTable
        fields = '__all__'