# Generated by Django 3.1.4 on 2020-12-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_user_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
