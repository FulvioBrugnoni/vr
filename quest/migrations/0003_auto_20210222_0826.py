# Generated by Django 3.1 on 2021-02-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0002_myuser_ruolo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
