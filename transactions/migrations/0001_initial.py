# Generated by Django 3.2.12 on 2022-04-01 08:50

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0004_auto_20220322_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SmallIntegerField(unique=True)),
                ('description', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField(verbose_name='Transaction Date')),
                ('description', models.CharField(max_length=200)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hours', models.DecimalField(decimal_places=1, max_digits=3)),
                ('amount_in', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('amount_out', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MaxValueValidator(Decimal('0'))])),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('accounting_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.accountingcode')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
