# Generated by Django 5.0 on 2024-01-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_alter_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(default='a0ae8a1ec54a3097029183b429efea59', max_length=32),
        ),
    ]
