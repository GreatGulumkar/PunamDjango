from rest_framework import serializers
from database.models import Sport


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ("sport_id", "image")
