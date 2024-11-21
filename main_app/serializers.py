from rest_framework import serializers
from .models import Artifact, Anomaly, Stalker


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = '__all__'


class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anomaly
        fields = '__all__'


class StalkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stalker
        fields = '__all__'