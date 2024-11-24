# Generated by Django 5.1.3 on 2024-11-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_nickname',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
