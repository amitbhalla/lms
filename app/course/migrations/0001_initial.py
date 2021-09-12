# Generated by Django 3.2.7 on 2021-09-12 11:46

import course.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-modified_date'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('instructor', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('tagline', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(default=0.0)),
                ('duration', models.IntegerField()),
                ('thumbnail', models.ImageField(upload_to=course.models.course_thumbnail)),
                ('resource', models.FileField(upload_to=course.models.course_resource)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.category')),
            ],
            options={
                'ordering': ['-modified_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='course.course')),
            ],
            options={
                'ordering': ['-modified_date'],
            },
        ),
    ]
