# Generated by Django 3.2 on 2024-06-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='country',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
