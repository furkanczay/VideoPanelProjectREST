# Generated by Django 4.2.2 on 2023-06-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_remove_videomodel_video_videomodel_video_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='created_on',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='updated_on',
            field=models.DateTimeField(editable=False),
        ),
    ]