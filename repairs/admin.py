from django.contrib import admin

from .models import Category, RepairImage, RepairRequest


class RepairImageInline(admin.TabularInline):
    model = RepairImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "customer",
        "category",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "category",
    )

    search_fields = (
        "title",
        "customer__username",
    )

    inlines = [RepairImageInline]