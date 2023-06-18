# Generated by Django 3.1.7 on 2021-07-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20210705_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='video_lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subject', models.TextField()),
                ('teacher', models.CharField(max_length=250)),
                ('video', models.FileField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]