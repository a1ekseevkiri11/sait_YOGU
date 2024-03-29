# Generated by Django 5.0 on 2024-03-19 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rejectioncomment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rejection_comment', to='showcase_projects.project'),
        ),
        migrations.AlterField(
            model_name='timepermission',
            name='group',
            field=models.CharField(choices=[('student', 'student'), ('lecturer', 'lecturer'), ('customer', 'customer'), ('administrator', 'administrator')], max_length=127),
        ),
    ]
