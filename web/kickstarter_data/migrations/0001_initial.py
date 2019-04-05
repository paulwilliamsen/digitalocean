# Generated by Django 2.2 on 2019-04-02 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('category', models.CharField(max_length=1024)),
                ('main_category', models.CharField(max_length=1024)),
                ('currency', models.CharField(max_length=1024)),
                ('deadline', models.CharField(max_length=1024)),
                ('goal', models.FloatField(verbose_name=0.0)),
                ('launched', models.CharField(max_length=1024)),
                ('pledged', models.FloatField(verbose_name=0.0)),
                ('state', models.CharField(max_length=1024)),
                ('backers', models.FloatField(verbose_name=0.0)),
                ('country', models.CharField(max_length=1024)),
                ('usd_pledged', models.FloatField(verbose_name=0.0)),
                ('usd_pledged_real', models.FloatField(verbose_name=0.0)),
                ('usd_goal_real', models.FloatField(verbose_name=0.0)),
            ],
        ),
    ]
