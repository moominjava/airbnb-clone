# Generated by Django 2.2.5 on 2020-11-04 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='usre',
            new_name='user',
        ),
    ]
