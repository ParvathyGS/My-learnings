# Generated by Django 2.0 on 2020-01-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PGFinder', '0003_auto_20191231_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pgname', models.CharField(default='Stella Dimora', max_length=100)),
                ('username', models.CharField(default='Parvathy', max_length=100)),
                ('notif_msg', models.CharField(default='Viewed your conatct information', max_length=200)),
            ],
        ),
    ]