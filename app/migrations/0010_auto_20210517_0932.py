# Generated by Django 3.2 on 2021-05-17 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_reg_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='admin',
        ),
        migrations.AlterField(
            model_name='reg',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reg',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
