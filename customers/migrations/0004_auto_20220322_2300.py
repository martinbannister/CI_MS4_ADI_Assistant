# Generated by Django 3.2.12 on 2022-03-22 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_rename_subjects_subject'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubjectCategories',
            new_name='SubjectCategory',
        ),
        migrations.AlterModelOptions(
            name='progress',
            options={'verbose_name_plural': 'Progress'},
        ),
        migrations.AlterModelOptions(
            name='subjectcategory',
            options={'verbose_name_plural': 'Subject Categories'},
        ),
    ]
