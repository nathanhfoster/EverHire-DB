# Generated by Django 2.1.2 on 2018-11-11 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20181110_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='longitude',
            new_name='lng',
        ),
    ]
