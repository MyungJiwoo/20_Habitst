# Generated by Django 3.1.1 on 2020-09-29 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0019_auto_20200929_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='other_id',
        ),
    ]