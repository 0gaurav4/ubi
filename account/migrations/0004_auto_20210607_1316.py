# Generated by Django 3.1.7 on 2021-06-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210607_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ppic',
            field=models.ImageField(default='media\\pic\\person.png', upload_to='pic'),
        ),
    ]
