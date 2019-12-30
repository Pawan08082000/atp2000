# Generated by Django 2.2.3 on 2019-07-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('contact_no', models.IntegerField()),
                ('address', models.CharField(max_length=90)),
            ],
        ),
    ]
