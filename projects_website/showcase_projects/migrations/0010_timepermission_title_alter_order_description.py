# Generated by Django 5.0 on 2024-04-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_projects', '0009_order_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='timepermission',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(),
        ),
    ]
