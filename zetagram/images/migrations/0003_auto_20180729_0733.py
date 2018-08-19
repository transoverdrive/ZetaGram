# Generated by Django 2.0.7 on 2018-07-29 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20180726_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='images.Image'),
        ),
        migrations.AlterField(
            model_name='like',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='images.Image'),
        ),
    ]