from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Category, RepairRequest
from .serializers import (
    CategorySerializer,
    RepairRequestSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class RepairRequestViewSet(viewsets.ModelViewSet):
    serializer_class = RepairRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            RepairRequest.objects
            .select_related("customer", "category")
            .prefetch_related("images")
        )

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)