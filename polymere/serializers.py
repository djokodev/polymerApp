from .models import Reaction
from rest_framework import serializers

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = "__all__"

    