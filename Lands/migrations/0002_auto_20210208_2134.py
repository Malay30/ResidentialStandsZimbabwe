# Generated by Django 3.1.6 on 2021-02-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='username',
            field=models.TextField(default='not set'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='profilePhoto',
            field=models.ImageField(upload_to='profiles/'),
        ),
    ]
