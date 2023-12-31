# Generated by Django 4.2.2 on 2023-06-14 12:52

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategoriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_categories_images/')),
            ],
            options={
                'verbose_name': 'Kurs Kategorisi',
                'verbose_name_plural': 'Kurs Kategorileri',
                'db_table': 'course_categories',
            },
        ),
        migrations.CreateModel(
            name='PeriodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Dönem',
                'verbose_name_plural': 'Dönemler',
                'db_table': 'courses_periods',
            },
        ),
        migrations.CreateModel(
            name='CoursesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='lesson_images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.coursecategoriesmodel')),
            ],
            options={
                'verbose_name': 'Sınıf',
                'verbose_name_plural': 'Sınıflar',
                'db_table': 'courses',
            },
        ),
    ]
