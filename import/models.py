from django.db import models

from bank_transactions.models import MutationType


class INGMutationType(models.Model):
    description = models.CharField(max_length=255)
    mutation_type = models.ForeignKey(MutationType, on_delete=models.PROTECT)

    def __str__(self):
        return self.description
