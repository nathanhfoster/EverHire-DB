# Generated by Django 2.1.1 on 2018-11-20 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_job_worker_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='worker_id',
            new_name='worker',
        ),
    ]