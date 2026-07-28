from django.contrib import admin

from .models import (
    Category,
    Brand,
    Device,
    RepairRequest,
    RepairImage,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "created_at",
    )
    search_fields = ("name",)
    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "created_at",
    )
    search_fields = ("name",)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "brand",
        "created_at",
    )
    search_fields = ("name",)


@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "customer",
        "category",
        "status",
        "priority",
        "created_at",
    )

    list_filter = (
        "status",
        "priority",
        "category",
    )

    search_fields = (
        "title",
        "description",
        "customer__username",
    )


@admin.register(RepairImage)
class RepairImageAdmin(admin.ModelAdmin):
    list_display = (
        "repair_request",
        "created_at",
    )