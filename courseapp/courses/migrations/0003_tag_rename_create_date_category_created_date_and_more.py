# Generated by Django 5.1.6 on 2025-02-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='category',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(upload_to='lessons/%Y/%m/'),
        ),
    ]
