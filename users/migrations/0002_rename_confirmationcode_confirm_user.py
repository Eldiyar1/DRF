# Generated by Django 4.1.5 on 2023-05-12 18:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConfirmationCode',
            new_name='Confirm_User',
        ),
    ]
