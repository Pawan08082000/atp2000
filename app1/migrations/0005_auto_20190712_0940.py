# Generated by Django 2.2.3 on 2019-07-12 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20190712_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_details',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]
