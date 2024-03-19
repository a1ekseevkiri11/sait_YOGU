# Generated by Django 5.0 on 2024-03-19 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('accepted', 'Принят'), ('processing', 'В обработке'), ('rejected', 'Отклонен')], default='processing', max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('place', models.IntegerField(default=6)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='registration.customer')),
                ('lecturer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer', to='registration.lecturer')),
            ],
            options={
                'permissions': [('change_status_project', 'Can change status project')],
            },
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.student')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase_projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='MotivationLetters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('accepted', 'Принят'), ('processing', 'В обработке'), ('rejected', 'Отклонен')], default='processing', max_length=20)),
                ('letter', models.FileField(upload_to='letters/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.student')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase_projects.project')),
            ],
            options={
                'permissions': [('download_motivationletters', 'Can download motivation letters'), ('change_status_motivationletters', 'Can change status motivation letters')],
            },
        ),
        migrations.CreateModel(
            name='RejectionComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rejection_comment', to='showcase_projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='TimePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[], max_length=127)),
                ('time_add', models.DateTimeField()),
                ('time_delete', models.DateTimeField()),
                ('completed_add', models.BooleanField(default=False)),
                ('completed_delete', models.BooleanField(default=False)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
            ],
        ),
        migrations.AddConstraint(
            model_name='timepermission',
            constraint=models.UniqueConstraint(fields=('permission', 'group'), name='unique_permission_group'),
        ),
    ]