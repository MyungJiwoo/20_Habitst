# Generated by Django 3.1.1 on 2020-09-30 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0020_auto_20200929_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]