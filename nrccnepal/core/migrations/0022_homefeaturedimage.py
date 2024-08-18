# Generated by Django 5.1 on 2024-08-17 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_upcomingprograms_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeFeaturedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landing_cover_pic', models.ImageField(upload_to='images/landing_page_images')),
                ('intro_side_pic', models.ImageField(upload_to='images/landing_page_images')),
            ],
        ),
    ]
