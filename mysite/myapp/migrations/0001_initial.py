# Generated by Django 5.1.5 on 2025-01-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('carbs', models.FloatField()),
                ('proteins', models.FloatField()),
                ('flats', models.FloatField()),
                ('calories', models.IntegerField()),
            ],
        ),
    ]
