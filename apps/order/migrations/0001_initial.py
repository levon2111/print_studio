# Generated by Django 2.1 on 2018-09-09 15:26

import apps.order.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HolderType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.HolderType')),
            ],
            options={
                'verbose_name_plural': 'Holder Type',
            },
        ),
        migrations.CreateModel(
            name='PhotoHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('prise', models.IntegerField()),
                ('photo', models.ImageField(upload_to=apps.order.models.get_file_path)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.HolderType')),
            ],
            options={
                'verbose_name_plural': 'Photo Holder',
            },
        ),
    ]
