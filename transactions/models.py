from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Transaction(models.Model):
    TYPE_CHOICES = [("expense", "Expense"), ("income", "Income")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    t_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-id"]

    def __str__(self):
        return f"{self.t_type} ₹{self.amount} on {self.date}"
