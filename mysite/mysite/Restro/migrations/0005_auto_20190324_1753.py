# Generated by Django 2.1.7 on 2019-03-24 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restro', '0004_auto_20190324_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='Restaurant_ID',
            field=models.CharField(max_length=100),
        ),
    ]
