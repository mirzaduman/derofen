# Generated by Django 3.2.6 on 2021-08-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakersoft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='verfugbar',
            field=models.BooleanField(default=True),
        ),
    ]
