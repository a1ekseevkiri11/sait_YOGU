# Generated by Django 5.0 on 2024-04-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_projects', '0008_delete_rejectioncomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(null=True),
        ),
    ]