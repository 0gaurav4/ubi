# Generated by Django 3.1.7 on 2021-06-14 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='User',
            new_name='user',
        ),
    ]
