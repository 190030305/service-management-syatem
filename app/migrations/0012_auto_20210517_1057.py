# Generated by Django 3.2 on 2021-05-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210517_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='fname',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AddField(
            model_name='reg',
            name='image',
            field=models.ImageField(default='null', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='reg',
            name='lname',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AddField(
            model_name='reg',
            name='password',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AddField(
            model_name='reg',
            name='typeo',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AddField(
            model_name='reg',
            name='uname',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='reg',
            name='answer',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='reg',
            name='email',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='reg',
            name='gender',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='reg',
            name='phone',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
