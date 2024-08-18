# Generated by Django 5.1 on 2024-08-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_homefeaturedimage_updated_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterMailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]
