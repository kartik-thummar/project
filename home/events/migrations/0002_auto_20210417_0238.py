# Generated by Django 3.1.7 on 2021-04-17 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Uncategarised', max_length=50),
        ),
    ]
