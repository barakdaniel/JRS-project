# Generated by Django 3.0.6 on 2020-07-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20200718_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='logo',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='rank',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
