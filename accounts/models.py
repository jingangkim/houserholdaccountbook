from django.db import models

from accounts.constants import BANK_CODES, TRANSACTION_TYPE

from users.models import User

# Create your models here.
# 2. **accounts**: 계좌 정보 관리
#    - 필드: 사용자, 계좌번호, 은행코드, 거래 타입, 잔고
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=30)
    bank_code = models.CharField(max_length=10, choices=BANK_CODES)
    TRANSACTION_TYPE = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
