# Generated by Django 3.1.1 on 2020-10-20 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True)),
                ('amount', models.PositiveIntegerField()),
                ('photo', models.ImageField(upload_to='')),
                ('date_select', models.DateTimeField(blank=True, null=True)),
                ('is_public', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hashtag_field', models.CharField(blank=True, max_length=200)),
                ('place', models.CharField(blank=True, max_length=200)),
                ('rule', models.TextField(blank=True)),
                ('max_p', models.PositiveIntegerField(default=1)),
                ('meet_id', models.PositiveIntegerField(default=0)),
                ('other_id', models.PositiveIntegerField(default=0)),
                ('member', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('imp_uid', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100, verbose_name='상품명')),
                ('amount', models.PositiveIntegerField(verbose_name='결제금액')),
                ('status', models.CharField(choices=[('ready', '미결제'), ('paid', '결제완료'), ('cancelled', '결제취소'), ('failed', '결제실패')], db_index=True, default='ready', max_length=9)),
                ('meta', jsonfield.fields.JSONField(blank=True, default={})),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
