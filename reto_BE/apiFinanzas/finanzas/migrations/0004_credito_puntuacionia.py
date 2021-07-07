# Generated by Django 3.2.5 on 2021-07-06 22:43

from django.db import migrations
import finanzas.utils


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0003_alter_credito_puntuacionsentinel'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='puntuacionIA',
            field=finanzas.utils.IntegerRangeField(default=5),
            preserve_default=False,
        ),
    ]
