from django.db import models

# Create your models here.

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type}: {self.description} - ${self.amount}"
