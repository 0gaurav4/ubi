# Generated by Django 3.1.7 on 2021-06-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210607_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ppic',
            field=models.ImageField(default='media\\default\\person.png', upload_to='pic'),
        ),
    ]
