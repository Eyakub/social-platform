# Generated by Django 3.0.6 on 2020-05-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_userprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
