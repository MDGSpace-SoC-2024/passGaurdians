# Generated by Django 5.0 on 2024-01-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(default='a47d30a9b62300b442c74a5e0ee4cffe', max_length=32),
        ),
    ]
