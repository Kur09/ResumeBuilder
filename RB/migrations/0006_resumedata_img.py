# Generated by Django 3.2.5 on 2021-10-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RB', '0005_auto_20211022_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumedata',
            name='img',
            field=models.ImageField(default=0, upload_to='RB/images'),
        ),
    ]
