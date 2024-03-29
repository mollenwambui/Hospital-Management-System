# Generated by Django 4.1.4 on 2022-12-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('middle_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField(null=True)),
                ('phone_number', models.CharField(max_length=10, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=12, null=True)),
                ('residential_address', models.CharField(max_length=20, null=True)),
                ('company', models.CharField(max_length=60, null=True)),
                ('insurance_id', models.CharField(max_length=20, null=True)),
                ('occupation', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
