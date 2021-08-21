from django.db import models
import math

class Produkt(models.Model):

    KATEGORIEN = (
        ('Brot', 'Brot'),
        ('Süßwaren', 'Süßwaren'),
        ('Kleingebäck', 'Kleingebäck')
    )

    GETREIDESORTEN = (
        ('Weizen', 'Weizen'),
        ('Roggen', 'Roggen'),
        ('Gerste', 'Gerste'),
        ('Hafer', 'Hafer'),
        ('Gerste', 'Gerste'),
        ('Mais', 'Mais'),
        ('Hirse', 'Hirse')
    )


    name = models.CharField(max_length=200)
    kategorie = models.CharField(max_length=200, choices=KATEGORIEN)
    getreide = models.CharField(max_length=200, blank=True, choices=GETREIDESORTEN)
    gewicht = models.IntegerField()
    kalorien_100g = models.IntegerField()
    kalorien_gesamt = models.IntegerField(editable=False)
    foto = models.ImageField(upload_to='fotos')
    verfugbar = models.BooleanField(default=True)
    gehen = models.IntegerField(editable=False)
    joggen = models.IntegerField(editable=False)


    def save(self, *args, **kwargs):
        a = self.kalorien_100g * (self.gewicht / 100 )
        self.kalorien_gesamt = a
        b = a / 5
        c = a / 11
        self.gehen = math.ceil(b)
        self.joggen = math.ceil(c)
        super(Produkt, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkte'


