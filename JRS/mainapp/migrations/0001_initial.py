# Generated by Django 3.0.6 on 2020-07-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jrsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=18)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=40)),
            ],
        ),
    ]
