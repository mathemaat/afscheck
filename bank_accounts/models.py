from django.db import models

from classes.Iban import Iban
from counterparties.models import Counterparty


class Bank(models.Model):
    name = models.CharField(max_length=255)
    iban_identifier = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    iban = models.CharField(max_length=255, unique=True, null=True, blank=True)
    number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)

    def __str__(self):
        if len(self.iban) >= 1:
            iban = Iban(self.iban)
            return str(iban)
        else:
            return self.number
