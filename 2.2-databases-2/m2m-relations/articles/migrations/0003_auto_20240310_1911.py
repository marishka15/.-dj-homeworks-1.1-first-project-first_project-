# Generated by Django 3.1.2 on 2024-03-10 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20240310_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='article',
            new_name='articles',
        ),
    ]
