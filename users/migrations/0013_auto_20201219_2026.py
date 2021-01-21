# Generated by Django 3.1.4 on 2020-12-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20201215_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'admin'), (2, 'doctor'), (3, 'patients')], default=3, null=True),
        ),
    ]
