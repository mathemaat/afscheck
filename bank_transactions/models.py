import hashlib

from django.db import models

from classes.Iban import Iban

from bank_accounts.models import BankAccount
from counterparties.models import Counterparty


class BankStatement(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT)
    upload_date = models.DateTimeField()
    period_start_date = models.DateField()
    period_end_date = models.DateField()
    transaction_count = models.IntegerField()
    transaction_amount = models.DecimalField(max_digits=8, decimal_places=2)


class ContraAccount(models.Model):
    description = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=255)
    counterparty = models.ForeignKey(Counterparty, on_delete=models.PROTECT, null=True, blank=True)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        unique_together = (("description", "bank_account_number"),)

    def __str__(self):
        if len(self.bank_account_number) >= 1:
            try:
                iban = Iban.parse_from_string(self.bank_account_number)
                bank_account_number = str(iban)
            except ValueError:
                bank_account_number = self.bank_account_number
            return '%s (%s)' % (self.description, bank_account_number)
        else:
            return self.description

    def get_md5_key(self):
        parts = (
            self.description,
            self.bank_account_number,
        )
        text = "-".join(parts)
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    def find_or_create(self):
        # check whether the contra account already exists in the database, otherwise create a new one
        try:
            existing = ContraAccount.objects.get(
                description=self.description,
                bank_account_number=self.bank_account_number,
            )
            return existing
        except ContraAccount.DoesNotExist:
            self.save()
            return self


class MutationType(models.Model):
    description = models.CharField(max_length=255)
    token = models.CharField(max_length=127)

    def __str__(self):
        return self.description


class INGMutationType(models.Model):
    description = models.CharField(max_length=255)
    mutation_type = models.ForeignKey(MutationType, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "ING mutation type"
        verbose_name_plural = "ING mutation types"

    def __str__(self):
        return self.description


class BankTransaction(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    bank_statement = models.ForeignKey(BankStatement, on_delete=models.PROTECT)
    contra_account = models.ForeignKey(ContraAccount, on_delete=models.PROTECT)
    mutation_type = models.ForeignKey(MutationType, on_delete=models.PROTECT)
