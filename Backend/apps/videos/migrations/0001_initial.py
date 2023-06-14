# Generated by Django 4.2.2 on 2023-06-14 12:52

import apps.videos.validators
import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('description', models.TextField()),
                ('video_file', models.FileField(null=True, upload_to='videos/', validators=[apps.videos.validators.validate_file_extension])),
                ('created_on', models.DateTimeField(editable=False)),
                ('updated_on', models.DateTimeField(editable=False)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='courses.coursesmodel')),
                ('instructor', models.ForeignKey(limit_choices_to={'groups': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videolar',
                'db_table': 'videos',
            },
        ),
        migrations.CreateModel(
            name='VideoCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_on', models.DateTimeField(editable=False)),
                ('updated_on', models.DateTimeField(editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='videos.videocommentmodel')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='videos.videomodel')),
            ],
            options={
                'verbose_name': 'Video Yorumu',
                'verbose_name_plural': 'Video Yorumları',
                'db_table': 'video_comments',
            },
        ),
    ]
