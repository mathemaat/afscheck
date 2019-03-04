# Generated by Django 2.1.6 on 2019-03-04 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank_transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='INGMutationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('mutation_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank_transactions.MutationType')),
            ],
        ),
    ]