from django.db import models

from accounts.models import Account

# Create your models here.


# 필드: 거래 발생 계좌, 거래 금액, 거래 후 잔액, 거래 상세 내역, 거래 유형, 거래 방식, 거래 날짜 및 시간
class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance_after = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_details = models.TextField()
    transaction_type = models.CharField(max_length=30)
    transaction_method = models.CharField(max_length=30)
    transaction_time = models.DateTimeField(auto_now_add=True)
