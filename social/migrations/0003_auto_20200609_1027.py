# Generated by Django 3.0.7 on 2020-06-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_comment_following_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='profile_pics/'),
        ),
    ]
