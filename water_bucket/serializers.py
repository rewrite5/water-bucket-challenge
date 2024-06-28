from rest_framework import serializers
from .models import WaterBucket


class WaterBucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterBucket
        fields = ["x", "y", "z"]
