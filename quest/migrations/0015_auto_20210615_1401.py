# Generated by Django 3.1 on 2021-06-15 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0014_amm1_lingua'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lingua', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quest.lingua')),
            ],
        ),
        migrations.CreateModel(
            name='Livello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lingua', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quest.lingua')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lingua', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quest.lingua')),
            ],
        ),
        migrations.CreateModel(
            name='Titolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lingua', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quest.lingua')),
            ],
        ),
        migrations.DeleteModel(
            name='Ambito',
        ),
        migrations.AlterModelOptions(
            name='studio',
            options={'verbose_name': 'studio', 'verbose_name_plural': 'studio'},
        ),
        migrations.RemoveField(
            model_name='candidatoesperienza',
            name='name',
        ),
        migrations.RemoveField(
            model_name='candidatoresidenza',
            name='amm5',
        ),
        migrations.RemoveField(
            model_name='candidatoresidenza',
            name='name',
        ),
        migrations.AddField(
            model_name='candidatoesperienza',
            name='candidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='candidatoresidenza',
            name='candidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='professione',
            name='lingua',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quest.lingua'),
        ),
        migrations.AddField(
            model_name='settore',
            name='lingua',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quest.lingua'),
        ),
        migrations.AlterField(
            model_name='linguaconosciuta',
            name='candidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='professione',
            name='settore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quest.settore'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='candidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='studio',
            table='studio',
        ),
        migrations.DeleteModel(
            name='Amm5',
        ),
        migrations.AddField(
            model_name='studio',
            name='materia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='quest.materia'),
        ),
        migrations.AlterField(
            model_name='linguaconosciuta',
            name='lingua',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quest.lang'),
        ),
        migrations.AlterField(
            model_name='linguaconosciuta',
            name='livello',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quest.livello'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='titolo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='quest.titolo'),
        ),
    ]
