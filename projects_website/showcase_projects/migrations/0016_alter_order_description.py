# Generated by Django 5.0 on 2024-04-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_projects', '0015_alter_timepermission_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
