# Generated by Django 3.1.7 on 2021-07-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
