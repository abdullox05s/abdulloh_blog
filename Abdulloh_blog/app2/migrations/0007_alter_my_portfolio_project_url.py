# Generated by Django 4.2.3 on 2023-07-16 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0006_remove_my_images_img2_remove_my_images_img3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_portfolio',
            name='project_url',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
