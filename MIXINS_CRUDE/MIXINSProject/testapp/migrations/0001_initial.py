# Generated by Django 2.2 on 2020-03-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField()),
                ('mname', models.CharField(max_length=30)),
                ('mprice', models.IntegerField()),
                ('mbaterry', models.IntegerField()),
                ('mcom', models.CharField(max_length=30)),
            ],
        ),
    ]