# Generated by Django 3.1 on 2021-02-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0013_auto_20210224_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(default=3, max_length=23),
            preserve_default=False,
        ),
    ]
