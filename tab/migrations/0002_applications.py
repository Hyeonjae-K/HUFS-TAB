# Generated by Django 4.0.1 on 2022-01-26 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.FileField(upload_to='applications/%Y-%m')),
            ],
        ),
    ]