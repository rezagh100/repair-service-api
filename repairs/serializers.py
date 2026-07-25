from rest_framework import serializers

from .models import Category, RepairImage, RepairRequest


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class RepairImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairImage
        fields = (
            "id",
            "image",
            "created_at",
        )
        read_only_fields = (
            "id",
            "created_at",
        )


class RepairRequestSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)
    images = RepairImageSerializer(many=True, read_only=True)

    class Meta:
        model = RepairRequest
        fields = (
            "id",
            "customer",
            "category",
            "title",
            "description",
            "address",
            "city",
            "status",
            "images",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "customer",
            "status",
            "created_at",
            "updated_at",
        )