# Generated by Django 3.2.5 on 2021-07-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0002_auto_20210706_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='puntuacionSentinel',
            field=models.CharField(choices=[('mala', 'mala'), ('regular', 'regular'), ('buena', 'buena')], default='regular', max_length=7),
        ),
    ]