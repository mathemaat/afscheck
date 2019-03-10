from django.db import models

from bank_accounts.models import BankAccount
from bank_transactions.models import MutationType
from counterparties.models import Counterparty


class ContraAccount(models.Model):
    description = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=255)
    counterparty = models.ForeignKey(Counterparty, on_delete=models.PROTECT)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        unique_together = (("description", "bank_account_number"),)

    def __str__(self):
        if len(self.bank_account_number) >= 1:
            return '%s (%s)' % (self.description, self.bank_account_number)
        else:
            return self.description


class INGMutationType(models.Model):
    description = models.CharField(max_length=255)
    mutation_type = models.ForeignKey(MutationType, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "ING mutation type"
        verbose_name_plural = "ING mutation types"

    def __str__(self):
        return self.description
