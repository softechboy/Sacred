# Generated by Django 3.1.1 on 2021-01-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='', upload_to='users')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
