# Generated by Django 3.0.2 on 2020-01-27 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('start_date', models.DateField()),
                ('start_weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet_id', models.IntegerField()),
                ('current_date', models.DateField()),
                ('current_weight', models.FloatField()),
            ],
        ),
    ]
