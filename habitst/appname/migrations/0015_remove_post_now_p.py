# Generated by Django 3.1.1 on 2020-09-29 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0014_auto_20200929_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='now_p',
        ),
    ]