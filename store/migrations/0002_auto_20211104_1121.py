# Generated by Django 3.1 on 2021-11-04 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='job_title',
            new_name='category',
        ),
    ]