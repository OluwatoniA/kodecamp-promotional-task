# Generated by Django 4.0.4 on 2022-06-07 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_rename_full_name_doctor_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='patient_name',
        ),
    ]
