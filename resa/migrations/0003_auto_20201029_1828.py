# Generated by Django 3.1.2 on 2020-10-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resa', '0002_auto_20201029_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diver',
            name='reservation',
            field=models.ManyToManyField(to='resa.Dive'),
        ),
    ]