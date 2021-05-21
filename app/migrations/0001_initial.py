# Generated by Django 3.2 on 2021-05-16 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('answer', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='pics')),
                ('admin', models.BooleanField(default='False')),
            ],
        ),
    ]
