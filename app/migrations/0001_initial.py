# Generated by Django 4.0.1 on 2022-03-27 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
                ('father', models.CharField(max_length=23)),
                ('branch', models.CharField(max_length=23)),
                ('valid_up', models.CharField(max_length=23)),
                ('DOB', models.DateField(default='08/07/2004')),
                ('roll', models.CharField(max_length=34)),
            ],
        ),
    ]