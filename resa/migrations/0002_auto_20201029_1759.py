# Generated by Django 3.1.2 on 2020-10-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diver',
            name='reservation',
            field=models.ManyToManyField(blank=True, to='resa.Dive'),
        ),
    ]
