# Generated by Django 5.0.6 on 2024-10-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctorsregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=50)),
                ('Contact', models.BigIntegerField()),
                ('Address', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pin', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('Specialization', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='file')),
                ('qual', models.FileField(upload_to='file')),
                ('exp', models.FileField(upload_to='file')),
                ('uname', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('status', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
