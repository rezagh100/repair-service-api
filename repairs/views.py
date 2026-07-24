from django.db.migrations import serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RepairsRequest
from .serializers import RepairsSerializer
from repairs import serializers
from rest_framework import status

class RepairRequestListAPIView(APIView):

    def get(self, request):
        repaiers = RepairsRequest.objects.all()
        serializer = RepairsSerializer(repaiers, many=True)

        return Response(serializer.data)
    def post(self , request):
        serializer = RepairsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status = status.HTTP_200_OK )
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
