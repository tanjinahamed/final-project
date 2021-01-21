# Generated by Django 3.1.4 on 2020-12-30 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_delete_confirmotp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pm_village',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ps_village',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
