# Generated by Django 3.1.7 on 2021-04-19 09:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timeStamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
