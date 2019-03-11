from datetime import date, datetime

from classes.CSVParser import CSVParser

from bank_accounts.models import BankAccount
from bank_transactions.models import BankStatement, BankTransaction, ContraAccount, INGMutationType


class INGBankStatementParser(CSVParser):

    # definieer kolomnummers
    KOLOM_DATUM = 0
    KOLOM_NAAM_OMSCHRIJVING = 1
    KOLOM_REKENING = 2
    KOLOM_TEGENREKENING = 3
    KOLOM_CODE = 4
    KOLOM_AF_BIJ = 5
    KOLOM_BEDRAG = 6
    KOLOM_MUTATIESOORT = 7
    KOLOM_MEDEDELINGEN = 8

    def set_column_definitions(self):
        self.column_definitions = {
            self.KOLOM_DATUM: CSVParser.TYPE_DATE,
            self.KOLOM_NAAM_OMSCHRIJVING: CSVParser.TYPE_STRING,
            self.KOLOM_REKENING: CSVParser.TYPE_IBAN,
            self.KOLOM_TEGENREKENING: CSVParser.TYPE_STRING,
            self.KOLOM_CODE: CSVParser.TYPE_STRING,
            self.KOLOM_AF_BIJ: CSVParser.TYPE_STRING,
            self.KOLOM_BEDRAG: CSVParser.TYPE_FLOAT,
            self.KOLOM_MUTATIESOORT: CSVParser.TYPE_STRING,
            self.KOLOM_MEDEDELINGEN: CSVParser.TYPE_STRING,
        }

    def validate(self):
        pass

    def save_bank_statement(self):
        firstrow = self.rows[0]
        iban = firstrow[self.KOLOM_REKENING]
        bank_account = BankAccount.objects.get(
            iban = iban.value
        )
        mindate = date.max
        maxdate = date.min
        count = len(self.rows)
        sum = 0.0
        for row in self.rows:
            # update mindate (if necessary)
            if row[self.KOLOM_DATUM] < mindate:
                mindate = row[self.KOLOM_DATUM]
            # update maxdate (if necessary)
            if row[self.KOLOM_DATUM] > maxdate:
                maxdate = row[self.KOLOM_DATUM]
            # update sum
            amount = row[self.KOLOM_BEDRAG]
            if row[self.KOLOM_AF_BIJ].lower() == 'af':
                amount *= -1
            sum += amount
        bank_statement = BankStatement(
            bank_account = bank_account,
            upload_date = datetime.now(),
            period_start_date = mindate,
            period_end_date = maxdate,
            transaction_count = count,
            transaction_amount = sum,
        )
        bank_statement.save()
        return bank_statement

    def save_bank_transactions(self, bank_statement):
        contra_account_cache = {}
        for row in self.rows:
            # determine date
            date = row[self.KOLOM_DATUM].isoformat()
            # determine amount
            amount = row[self.KOLOM_BEDRAG]
            if row[self.KOLOM_AF_BIJ].lower() == 'af':
                amount *= -1
            # determine contra account
            contra_account = ContraAccount(
                description = row[self.KOLOM_NAAM_OMSCHRIJVING],
                bank_account_number = row[self.KOLOM_TEGENREKENING],
            )
            key = contra_account.get_md5_key()
            if key in contra_account_cache:
                # load contra account from cache if possible
                contra_account = contra_account_cache[key]
            else:
                # otherwise, find existing or create a new one
                contra_account = contra_account.find_or_create()
                contra_account_cache[key] = contra_account
            # determine mutation type
            ing_mutation_type = INGMutationType.objects.get(
                description = row[self.KOLOM_MUTATIESOORT],
            )
            mutation_type = ing_mutation_type.mutation_type
            # save the bank transaction
            bank_transaction = BankTransaction(
                bank_statement = bank_statement,
                date = date,
                amount = amount,
                contra_account = contra_account,
                mutation_type = mutation_type,
                memo = row[self.KOLOM_MEDEDELINGEN],
            )
            bank_transaction.save()
