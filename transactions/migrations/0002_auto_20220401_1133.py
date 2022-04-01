# Generated by Django 3.2.12 on 2022-04-01 11:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingcode',
            name='code',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='accountingcode',
            unique_together={('owner', 'code')},
        ),
    ]
