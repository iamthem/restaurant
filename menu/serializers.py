from rest_framework import serializers
from .models import MenuSections, Success

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSections 
        fields = ['id', 'name']

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

class SuccessSerializer(serializers.Serializer):

    success = serializers.BooleanField ()

