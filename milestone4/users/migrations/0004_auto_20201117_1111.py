# Generated by Django 3.1.2 on 2020-11-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_handlemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhistorymodel',
            name='contributor_author',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='searchhistorymodel',
            name='contributor_committeechair',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='searchhistorymodel',
            name='contributor_department',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='searchhistorymodel',
            name='date1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='searchhistorymodel',
            name='date2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='searchhistorymodel',
            name='description_degree',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
