# Generated by Django 4.1.2 on 2022-11-29 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='scholl',
            new_name='school',
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together={('ClassName', 'school')},
        ),
    ]
