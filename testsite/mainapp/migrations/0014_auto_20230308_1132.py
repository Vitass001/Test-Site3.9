# Generated by Django 3.2.7 on 2023-03-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_rename_title1_post_title2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title2',
        ),
        migrations.AddField(
            model_name='post',
            name='title1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
