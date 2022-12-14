# Generated by Django 4.1 on 2022-08-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RB', '0006_resumedata_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverLetter',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('phone', models.IntegerField(default=0)),
                ('job', models.CharField(max_length=200)),
                ('study', models.CharField(max_length=100)),
                ('strength', models.CharField(max_length=200)),
                ('exp', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
