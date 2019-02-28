# Generated by Django 2.1.6 on 2019-02-28 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank_accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField()),
                ('period_start_date', models.DateField()),
                ('period_end_date', models.DateField()),
                ('transaction_count', models.IntegerField()),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank_accounts.BankAccount')),
            ],
        ),
        migrations.CreateModel(
            name='BankTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bank_statement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank_transactions.BankStatement')),
                ('contra_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank_accounts.BankAccount')),
            ],
        ),
        migrations.CreateModel(
            name='MutationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=127)),
            ],
        ),
        migrations.AddField(
            model_name='banktransaction',
            name='mutation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank_transactions.MutationType'),
        ),
    ]