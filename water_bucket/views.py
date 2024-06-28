from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import WaterBucket
from .serializers import WaterBucketSerializer
from modules.water_bucket import water_bucket_solver


class WaterBucketViewSet(ViewSet):
    queryset = WaterBucket.objects.all()
    serializer_class = WaterBucketSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            x = serializer.validated_data["x"]
            y = serializer.validated_data["y"]
            z = serializer.validated_data["z"]
            result = water_bucket_solver(x, y, z)
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
