# Generated by Django 3.0.7 on 2020-07-06 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('trackid', models.IntegerField(default=True)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
    ]
