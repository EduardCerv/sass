from rest_framework import serializers
from . import models


class FamiliSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'family_name', 'alias', 'created_at', 'updated_at',)
        model = models.Family
