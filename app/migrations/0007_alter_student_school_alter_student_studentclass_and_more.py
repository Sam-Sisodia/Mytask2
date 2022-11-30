# Generated by Django 4.1.2 on 2022-11-30 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_student_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='School',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='School_Student', to='app.school'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentclass',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_class', to='app.class'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_school', to=settings.AUTH_USER_MODEL),
        ),
    ]
