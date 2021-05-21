# Generated by Django 3.2 on 2021-05-16 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='answer',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='first_name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registration',
            name='last_name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registration',
            name='password',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.TextField(max_length=12),
        ),
        migrations.AlterField(
            model_name='registration',
            name='username',
            field=models.TextField(max_length=20),
        ),
    ]
