# Generated by Django 3.0.7 on 2020-06-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekrutacja', '0005_formucznia_pesel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formucznia',
            name='pesel',
            field=models.IntegerField(max_length=3),
        ),
    ]
