# Generated by Django 3.0.7 on 2020-06-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekrutacja', '0007_formucznia_miejsce_urodzenia'),
    ]

    operations = [
        migrations.AddField(
            model_name='formucznia',
            name='wojewodztwo',
            field=models.CharField(default='DS', max_length=2),
            preserve_default=False,
        ),
    ]