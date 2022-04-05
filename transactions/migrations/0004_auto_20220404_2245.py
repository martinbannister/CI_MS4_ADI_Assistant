# Generated by Django 3.2.12 on 2022-04-04 22:45

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20220322_2300'),
        ('transactions', '0003_auto_20220401_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount_in',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount_out',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='hours',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
