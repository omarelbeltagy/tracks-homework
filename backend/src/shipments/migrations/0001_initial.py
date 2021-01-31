# Generated by Django 3.1.5 on 2021-01-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.IntegerField()),
                ('co2', models.DecimalField(decimal_places=13, max_digits=17)),
                ('distance', models.DecimalField(decimal_places=14, max_digits=17)),
                ('avgWeight', models.DecimalField(decimal_places=15, max_digits=17)),
                ('intensityFactor', models.DecimalField(decimal_places=13, max_digits=17)),
                ('typeOfCalculation', models.CharField(max_length=7)),
                ('goodsType', models.CharField(max_length=9)),
                ('startCity', models.CharField(max_length=9)),
                ('endCity', models.CharField(max_length=9)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
