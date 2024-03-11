
# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.


# Create your models here.
class daily_expense_database(models.Model):
    food = models.DecimalField(max_digits=10, decimal_places=2)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    entertainment = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Financial Data for {self.created_at}"

