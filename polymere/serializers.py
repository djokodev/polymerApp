from .models import Polymer
from rest_framework import serializers

class PolymerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polymer
        fields = '__all__'

        