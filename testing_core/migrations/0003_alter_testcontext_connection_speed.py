# Generated by Django 5.2.4 on 2025-07-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_core', '0002_remove_app_test_platform_remove_teststatus_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcontext',
            name='connection_speed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
