# Generated by Django 5.0 on 2023-12-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='Emp_email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='emp',
            name='Emp_phn',
            field=models.CharField(max_length=100),
        ),
    ]
