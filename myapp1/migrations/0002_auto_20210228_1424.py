# Generated by Django 3.1 on 2021-02-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dateOfBirth',
            field=models.CharField(max_length=12),
        ),
    ]
