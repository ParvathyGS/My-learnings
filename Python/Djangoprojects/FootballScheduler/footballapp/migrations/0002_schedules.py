# Generated by Django 2.0 on 2020-05-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamName1', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time', models.DateTimeField()),
                ('Venue', models.CharField(max_length=100)),
            ],
        ),
    ]
