# Generated by Django 5.0.6 on 2024-06-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SharedFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('expiration_time', models.DateTimeField()),
            ],
        ),
    ]
