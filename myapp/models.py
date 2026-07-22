from django.db import models
from django.contrib.auth.models import User

class MonthlyPayment(models.Model):
        # 4 main data fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.user.username} - {self.amount}"