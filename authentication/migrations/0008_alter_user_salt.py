# Generated by Django 5.0 on 2024-01-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(default='d8b8cbe668c9ad3e8b72a38e423714a3', max_length=32),
        ),
    ]
