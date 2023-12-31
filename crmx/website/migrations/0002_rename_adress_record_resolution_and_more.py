# Generated by Django 5.0 on 2023-12-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='adress',
            new_name='resolution',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='phone',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='record',
            name='city',
        ),
        migrations.RemoveField(
            model_name='record',
            name='state',
        ),
        migrations.RemoveField(
            model_name='record',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='record',
            name='comment',
            field=models.TextField(default='', max_length=50000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='subject',
            field=models.TextField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
