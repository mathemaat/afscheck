from classes.CSVParser import CSVParser


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
