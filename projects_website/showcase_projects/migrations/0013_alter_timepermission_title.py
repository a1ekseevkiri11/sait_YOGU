# Generated by Django 5.0 on 2024-04-15 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_projects', '0012_alter_timepermission_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timepermission',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
