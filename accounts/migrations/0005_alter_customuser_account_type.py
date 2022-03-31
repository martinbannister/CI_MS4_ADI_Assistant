# Generated by Django 3.2.12 on 2022-03-31 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220331_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_type',
            field=models.IntegerField(choices=[(0, 'PDI'), (1, 'ADI'), (2, 'Pupil')]),
        ),
    ]
