# Generated by Django 3.1 on 2021-02-23 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_auto_20210223_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.branch'),
        ),
    ]
