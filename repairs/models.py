import uuid

from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        unique=True
    )

    icon = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Brand(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=100,
        unique=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="brands"
    )

    def __str__(self):
        return self.name


class Device(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=150
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="devices"
    )

    def __str__(self):
        return self.name


class RepairRequest(TimeStampedModel):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        WAITING_FOR_OFFERS = "waiting_for_offers", "Waiting For Offers"
        ACCEPTED = "accepted", "Accepted"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"
        CANCELED = "canceled", "Canceled"


    class Priority(models.TextChoices):
        LOW = "low", "Low"
        NORMAL = "normal", "Normal"
        HIGH = "high", "High"
        URGENT = "urgent", "Urgent"


    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="repair_requests",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="repair_requests",
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name="repair_requests",
        null=True,
        blank=True,
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.PROTECT,
        related_name="repair_requests",
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    preferred_time = models.DateTimeField(
        null=True,
        blank=True
    )

    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.NORMAL,
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.PENDING,
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class RepairImage(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    repair_request = models.ForeignKey(
        RepairRequest,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="repair_requests/"
    )

    def __str__(self):
        return f"Image - {self.repair_request.title}"