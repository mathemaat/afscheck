INSERT INTO bank_accounts_bank (name, iban_identifier)
VALUES
  ('ING', 'INGB'),
  ('Triodos', 'TRIO');

INSERT INTO bank_accounts_bankaccount (iban, bank_id)
VALUES
  ('NL08INGB0009347669', (SELECT id FROM bank_accounts_bank WHERE iban_identifier = 'INGB')),
  ('NL63TRIO0379393549', (SELECT id FROM bank_accounts_bank WHERE iban_identifier = 'TRIO'));

INSERT INTO bank_transactions_mutationtype (description, token)
VALUES
  ('Pinnen', 'WITHDRAWAL'),
  ('Storten', 'DEPOSIT'),
  ('PIN-betaling', 'PIN_PAYMENT'),
  ('Online bankieren', 'ONLINE_BANKING'),
  ('Incasso', 'DEBT_COLLECTION');

INSERT INTO bank_transactions_ingmutationtype (description, mutation_type_id)
VALUES
  ('geldautomaat',     (SELECT id FROM bank_transactions_mutationtype WHERE token = 'WITHDRAWAL')),
  ('storting',         (SELECT id FROM bank_transactions_mutationtype WHERE token = 'DEPOSIT')),
  ('betaalautomaat',   (SELECT id FROM bank_transactions_mutationtype WHERE token = 'PIN_PAYMENT')),
  ('verzamelbetaling', (SELECT id FROM bank_transactions_mutationtype WHERE token = 'ONLINE_BANKING')),
  ('online bankieren', (SELECT id FROM bank_transactions_mutationtype WHERE token = 'ONLINE_BANKING')),
  ('overschrijving',   (SELECT id FROM bank_transactions_mutationtype WHERE token = 'ONLINE_BANKING')),
  ('incasso',          (SELECT id FROM bank_transactions_mutationtype WHERE token = 'DEBT_COLLECTION')),
  ('diversen',         (SELECT id FROM bank_transactions_mutationtype WHERE token = 'DEBT_COLLECTION'));
