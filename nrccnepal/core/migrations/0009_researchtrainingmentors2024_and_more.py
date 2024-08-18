# Generated by Django 5.1 on 2024-08-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_researchtrainingmentors2023_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchTrainingMentors2024',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Mentors Name, along with academic qualification')),
                ('affiliation', models.CharField(max_length=100, verbose_name='Affiliation')),
                ('social_link', models.CharField(max_length=200)),
                ('social', models.CharField(choices=[('LI', 'LinkedIn'), ('FB', 'Facebook'), ('EM', 'Email')], max_length=2)),
                ('priority', models.PositiveIntegerField(default=0, verbose_name='Order in Mentors List')),
                ('image', models.ImageField(upload_to='images/rt_2024/rt_mentors__2024')),
            ],
            options={
                'ordering': ['priority', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ResearchTrainingOrganizers2024',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Organizer Name')),
                ('priority', models.PositiveIntegerField(default=0, verbose_name='Order in Organizers List')),
                ('image', models.ImageField(upload_to='images/rt_2024/rt_organizers__2024')),
            ],
            options={
                'ordering': ['priority', 'name'],
            },
        ),
        migrations.RenameField(
            model_name='researchtrainingmentors2023',
            old_name='trainer_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='researchtrainingmentors2023',
            old_name='social_flag',
            new_name='social',
        ),
        migrations.RenameField(
            model_name='researchtrainingorganizers2023',
            old_name='trainer_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='researchtrainingtrainers2023',
            old_name='trainer_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='researchtrainingtrainers2023',
            old_name='social_flag',
            new_name='social',
        ),
        migrations.RemoveField(
            model_name='researchtrainingtrainers2024',
            name='trainer_image',
        ),
        migrations.AddField(
            model_name='researchtrainingtrainers2024',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/rt_2024/rt_trainers_2024'),
        ),
    ]
