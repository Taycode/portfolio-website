# Generated by Django 3.0.2 on 2020-02-01 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
        ),
    ]
