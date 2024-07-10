# Generated by Django 5.0.7 on 2024-07-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='created',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.CharField(default='George Orwell', max_length=500),
        ),
        migrations.AddField(
            model_name='item',
            name='pages',
            field=models.IntegerField(default=328),
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(default='1984', max_length=200),
        ),
    ]