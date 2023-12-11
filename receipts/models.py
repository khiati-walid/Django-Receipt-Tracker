from django.db import models
from django.contrib.auth.models import User


class Receipt(models.Model):
    store_name = models.CharField(max_length=255)
    date_of_purchase = models.DateField()
    item_list = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store_name} - {self.date_of_purchase}"
