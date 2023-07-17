# Generated by Django 4.2 on 2023-06-26 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subproject', '0002_regis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regis',
            old_name='HallName',
            new_name='HallID',
        ),
        migrations.RenameField(
            model_name='regis',
            old_name='LecturerName',
            new_name='LecturerID',
        ),
        migrations.RenameField(
            model_name='regis',
            old_name='ProgramName',
            new_name='ProgramID',
        ),
        migrations.RemoveField(
            model_name='regis',
            name='Capacity',
        ),
    ]
