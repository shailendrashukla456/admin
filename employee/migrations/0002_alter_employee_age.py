# Generated by Django 4.1.4 on 2022-12-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(max_length=2),
        ),
    ]
