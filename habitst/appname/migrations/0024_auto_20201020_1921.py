# Generated by Django 3.1.2 on 2020-10-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0023_auto_20201020_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
