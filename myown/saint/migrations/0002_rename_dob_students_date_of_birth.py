# Generated by Django 4.1.4 on 2023-02-01 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saint', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='dob',
            new_name='date_of_birth',
        ),
    ]