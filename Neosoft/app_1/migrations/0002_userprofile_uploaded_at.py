# Generated by Django 3.0.4 on 2020-03-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]