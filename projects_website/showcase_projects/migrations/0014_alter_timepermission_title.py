# Generated by Django 5.0 on 2024-04-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_projects', '0013_alter_timepermission_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timepermission',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
