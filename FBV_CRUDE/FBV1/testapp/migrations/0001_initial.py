# Generated by Django 2.2 on 2020-03-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=30)),
                ('eid', models.IntegerField()),
                ('esal', models.IntegerField()),
                ('eaddr', models.CharField(max_length=30)),
            ],
        ),
    ]
