# Generated by Django 3.2.6 on 2021-08-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakersoft', '0002_produkt_verfugbar'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='gehen',
            field=models.IntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produkt',
            name='joggen',
            field=models.IntegerField(default=1, editable=False),
            preserve_default=False,
        ),
    ]