# Generated by Django 5.0 on 2024-01-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_alter_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(default='1ccff2daa43dd163dd0d7dd60be65fdb', max_length=32),
        ),
    ]
