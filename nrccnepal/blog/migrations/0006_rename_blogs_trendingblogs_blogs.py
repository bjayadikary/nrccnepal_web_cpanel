# Generated by Django 4.1.7 on 2023-03-25 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_blog_priority_blogs_priority_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trendingblogs',
            old_name='Blogs',
            new_name='blogs',
        ),
    ]
