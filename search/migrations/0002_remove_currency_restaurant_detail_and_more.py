# Generated by Django 4.2.2 on 2023-06-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='restaurant_detail',
        ),
        migrations.AddField(
            model_name='restaurantdetail',
            name='currency',
            field=models.ManyToManyField(to='search.currency'),
        ),
    ]