# Generated by Django 2.0.7 on 2018-08-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20180811_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('like', 'Like'), ('comment', 'Comment'), ('follow', 'Follow')], max_length=20),
        ),
    ]
