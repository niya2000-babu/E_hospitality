# Generated by Django 5.0.6 on 2024-10-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=25)),
                ('Date', models.DateField()),
                ('Symptoms', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=15)),
                ('status', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='patientregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Address', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Contact', models.BigIntegerField()),
                ('Age', models.BigIntegerField(default=0)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('status', models.CharField(default='', max_length=20)),
            ],
        ),
    ]