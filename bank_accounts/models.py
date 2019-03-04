from django.db import models

from counterparties.models import Counterparty


class Bank(models.Model):
    name = models.CharField(max_length=255)
    iban_identifier = models.CharField(max_length=4)


class BankAccount(models.Model):
    iban = models.CharField(max_length=255, unique=True, null=True, blank=True)
    number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    counterparty = models.ForeignKey(Counterparty, on_delete=models.PROTECT, null=True, blank=True)
