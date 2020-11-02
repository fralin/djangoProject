from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.


class Site(models.Model):
    """
    Description des sites de plongée dispo
    name : nom du site
    description : Description du site de plangée
    depth : profondeur maximum du site
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    depth = models.IntegerField()

    class Meta:
        ordering = ('name', 'depth',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resa:site_detail', args=[self.id])


class Dive(models.Model):
    """
    Description des sites de plongée prévues
    - date : date de la plongée
    - site : nom du site prévu
    - nbPlaces : nombre de places disponibles
    """

    date = models.DateTimeField()
    site = models.ForeignKey(Site,
                             on_delete=models.CASCADE,
                             related_name='site_dives')
    nbPlaces = models.IntegerField()

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.site.name + str(self.date)


class Diver(AbstractUser):
    LEVEL_CHOICES = (
        ('P0', 'Aucun'),
        ('P1', 'Niveau 1'),
        ('P2', 'Niveau 2'),
        ('P3', 'Niveau 3'),
        ('E2', 'MF1'),
        ('E3', 'MF2'),
    )
    level = models.CharField(max_length=2,
                             choices=LEVEL_CHOICES,
                             default='P0')
    birth_date = models.DateField(null=True, blank=True)
    reservation = models.ManyToManyField(Dive, blank=True)

    class Meta:
        ordering = ('last_name', 'level',)

    def __str__(self):
        return self.last_name + self.first_name
