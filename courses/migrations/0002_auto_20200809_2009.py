# Generated by Django 3.1 on 2020-08-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.CharField(max_length=15)),
                ('real_name', models.CharField(max_length=30)),
                ('tz', models.CharField(max_length=30)),
                ('activity_periods', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
