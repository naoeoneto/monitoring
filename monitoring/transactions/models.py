from django.db import models


# Create your models here.
class TransactionStatus(models.TextChoices):
    APPROVED = "approved"
    BACKEND_REVERSED = "backend_reversed"
    DENIED = "denied"
    FAILED = "failed"
    PROCESSING = "processing"
    REFUNDED = "refunded"
    REVERSED = "reversed"


class Transaction(models.Model):
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=TransactionStatus.choices,
        default=TransactionStatus.PROCESSING,
    )
    count = models.IntegerField(null=True)
