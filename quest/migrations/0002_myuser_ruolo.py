# Generated by Django 3.1 on 2021-02-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='ruolo',
            field=models.PositiveSmallIntegerField(choices=[(1, 'recruiter'), (2, 'studente')], default=1),
            preserve_default=False,
        ),
    ]
