from classes.CSVParser import CSVParser

from bank_transactions.models import ContraAccount


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

    def handle_contra_accounts(self):
        contra_accounts = {}
        for row in self.rows:
            contra_account = ContraAccount(
                description = row[self.KOLOM_NAAM_OMSCHRIJVING],
                bank_account_number = row[self.KOLOM_TEGENREKENING],
            )
            key = contra_account.get_md5_key()
            # continue with the next row if we encountered this contra account before
            if key in contra_accounts:
                continue
            # check whether the contra account already exists in the database
            try:
                existing = ContraAccount.objects.get(
                    description=contra_account.description,
                    bank_account_number=contra_account.bank_account_number,
                )
                contra_accounts[key] = existing
            except ContraAccount.DoesNotExist:
                contra_accounts[key] = contra_account
        return contra_accounts
