# Generated by Django 4.2.3 on 2023-07-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_my_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_images',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='my_images',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='my_images',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='my_images',
            name='img5',
        ),
        migrations.AlterField(
            model_name='my_images',
            name='img1',
            field=models.FileField(default=None, null=True, upload_to='my_pictures'),
        ),
    ]
