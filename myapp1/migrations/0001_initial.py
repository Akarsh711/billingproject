# Generated by Django 3.1.4 on 2021-02-01 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('e_id', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=25)),
                ('dob', models.DateTimeField()),
                ('salary', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
                ('rollno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='studentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=23)),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
                ('rollno', models.IntegerField()),
                ('stu_class', models.CharField(max_length=23)),
                ('f_name', models.CharField(max_length=23)),
                ('m_name', models.CharField(max_length=23)),
                ('dateOfBirth', models.DateTimeField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentFeesDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenanceCharges1', models.IntegerField(null=True)),
                ('examFee', models.IntegerField(null=True)),
                ('libraryCharges', models.IntegerField(null=True)),
                ('totalFee', models.IntegerField()),
                ('pay_date', models.DateTimeField()),
                ('tutionFee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.studentcourse')),
            ],
        ),
    ]
