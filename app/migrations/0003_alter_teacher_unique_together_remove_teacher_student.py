# Generated by Django 4.1.2 on 2022-11-29 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_scholl_class_school_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teacher',
            unique_together={('School', 'user')},
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='student',
        ),
    ]