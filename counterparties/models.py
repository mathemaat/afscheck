from django.db import models


class CounterpartyType(models.Model):
    description = models.CharField(max_length=255)
    token = models.CharField(max_length=127)

    def __str__(self):
        return self.description


class Counterparty(models.Model):
    name = models.CharField(max_length=255)
    counter_party_type = models.ForeignKey(CounterpartyType, on_delete=models.PROTECT)

    def __str__(self):
        return '%s (%s)' % (self.name, CounterpartyType.description)
