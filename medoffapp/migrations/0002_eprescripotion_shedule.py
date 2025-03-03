# Generated by Django 5.0.4 on 2024-10-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medoffapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='eprescripotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Age', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=20)),
                ('Medicines', models.CharField(max_length=50)),
                ('Test', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='shedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Age', models.CharField(max_length=50, null=True)),
                ('Contact', models.CharField(max_length=50, null=True)),
                ('Email', models.CharField(max_length=50, null=True)),
                ('Gender', models.CharField(max_length=20, null=True)),
                ('Time', models.TimeField(max_length=20, null=True)),
                ('bill', models.IntegerField(null=True)),
            ],
        ),
    ]
