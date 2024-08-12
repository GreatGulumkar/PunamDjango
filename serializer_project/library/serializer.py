from rest_framework import serializers

from .models import Books


class Books_serializer(serializers.ModelSerializer):
    class Meta:
        model = Books

        fields = "__all__"  # ["name", "Auther"]

    def validate_edition(self, value):
        if value < 1:
            raise serializers.ValidationError("Editoin must be greater than 1")
        return value
