# Generated by Django 5.0 on 2024-04-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_projects', '0018_alter_order_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='timepermission',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
