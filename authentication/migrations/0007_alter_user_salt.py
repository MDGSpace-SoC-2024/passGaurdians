# Generated by Django 5.0 on 2024-01-21 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(default='38a2a5e247e615e9d30056bf42e7118c', max_length=32),
        ),
    ]
