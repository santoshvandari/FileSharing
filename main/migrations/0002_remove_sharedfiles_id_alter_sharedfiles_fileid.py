# Generated by Django 5.0.6 on 2024-06-12 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharedfiles',
            name='id',
        ),
        migrations.AlterField(
            model_name='sharedfiles',
            name='fileid',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
