# Generated by Django 3.0.8 on 2020-08-27 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0002_auto_20200813_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialPlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(default=0, max_length=20)),
            ],
            options={
                'db_table': 'social_platform',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_login_id', models.CharField(blank=True, max_length=50)),
                ('social', models.ForeignKey(blank=True, default=1, max_length=20, on_delete=django.db.models.deletion.CASCADE, to='appname.SocialPlatform')),
            ],
        ),
    ]
