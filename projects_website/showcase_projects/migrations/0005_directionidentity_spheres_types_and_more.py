# Generated by Django 5.0 on 2024-04-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_projects', '0004_rename_time_add_timepermission_time_finish_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectionIdentity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Spheres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='customer_type',
            field=models.CharField(choices=[('external', 'Внешний'), ('interior', 'Внутренний')], default='processing', max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='directionIdentity',
            field=models.ManyToManyField(to='showcase_projects.directionidentity'),
        ),
        migrations.AddField(
            model_name='project',
            name='spheres',
            field=models.ManyToManyField(to='showcase_projects.spheres'),
        ),
        migrations.AddField(
            model_name='project',
            name='types',
            field=models.ManyToManyField(to='showcase_projects.types'),
        ),
    ]