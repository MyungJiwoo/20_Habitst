# Generated by Django 2.2.8 on 2020-09-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0006_merge_20200917_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
