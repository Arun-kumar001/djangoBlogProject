# Generated by Django 4.0.6 on 2022-08-08 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_about',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=80),
        ),
    ]