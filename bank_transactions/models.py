from django.db import models

from bank_accounts.models import BankAccount


class BankStatement(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT)
    upload_date = models.DateTimeField()
    period_start_date = models.DateField()
    period_end_date = models.DateField()
    transaction_count = models.IntegerField()
    transaction_amount = models.DecimalField(max_digits=8, decimal_places=2)


class MutationType(models.Model):
    description = models.CharField(max_length=255)
    token = models.CharField(max_length=127)

    def __str__(self):
        return self.description


class BankTransaction(models.Model):
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    bank_statement = models.ForeignKey(BankStatement, on_delete=models.PROTECT)
    contra_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT)
    mutation_type = models.ForeignKey(MutationType, on_delete=models.PROTECT)
