# Generated by Django 3.2.6 on 2022-11-08 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio_virtual', '0002_item_curtidas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temperatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'db_table': 'temperatura',
            },
        ),
    ]
