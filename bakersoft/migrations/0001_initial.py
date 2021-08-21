# Generated by Django 3.2.6 on 2021-08-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kategorie', models.CharField(choices=[('Brot', 'Brot'), ('Süßwaren', 'Süßwaren'), ('Kleingebäck', 'Kleingebäck')], max_length=200)),
                ('getreide', models.CharField(blank=True, choices=[('Weizen', 'Weizen'), ('Roggen', 'Roggen'), ('Gerste', 'Gerste'), ('Hafer', 'Hafer'), ('Gerste', 'Gerste'), ('Mais', 'Mais'), ('Hirse', 'Hirse')], max_length=200)),
                ('gewicht', models.IntegerField()),
                ('kalorien_100g', models.IntegerField()),
                ('kalorien_gesamt', models.IntegerField(editable=False)),
                ('foto', models.ImageField(upload_to='fotos')),
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkte',
                'ordering': ['-id'],
            },
        ),
    ]
