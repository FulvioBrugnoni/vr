# Generated by Django 3.1 on 2021-02-16 14:20

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AziendaLingua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('azienda', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'azienda',
                'verbose_name_plural': 'aziende',
                'db_table': 'azienda',
            },
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'candidato',
                'verbose_name_plural': 'candidati',
                'db_table': 'candidato',
            },
        ),
        migrations.CreateModel(
            name='Domanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chiave', models.CharField(max_length=6, unique=True)),
                ('testo', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'verbose_name': 'domanda',
                'verbose_name_plural': 'domande',
                'db_table': 'domanda',
            },
        ),
        migrations.CreateModel(
            name='GestioneInserimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passo_corrente', models.CharField(max_length=256)),
                ('passo_destra', models.CharField(max_length=256)),
                ('passo_sinistra', models.CharField(max_length=256)),
                ('slide', models.IntegerField()),
            ],
            options={
                'verbose_name': 'gestione_inserimenti',
                'verbose_name_plural': 'gestioni_inserimenti',
                'db_table': 'gestione_inserimenti',
            },
        ),
        migrations.CreateModel(
            name='Lingua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lingua', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'lingua',
                'verbose_name_plural': 'lingue',
                'db_table': 'lingua',
            },
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'verbose_name': 'questionario',
                'verbose_name_plural': 'questionari',
                'db_table': 'questionario',
            },
        ),
        migrations.CreateModel(
            name='QuestionarioDomanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posizione', models.PositiveSmallIntegerField()),
                ('domanda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.domanda')),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.questionario')),
            ],
            options={
                'verbose_name': 'questionario_domanda',
                'verbose_name_plural': 'questionari_domanda',
                'db_table': 'questionario_domanda',
                'unique_together': {('questionario', 'posizione'), ('questionario', 'domanda')},
            },
        ),
        migrations.CreateModel(
            name='Testo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testo', models.CharField(max_length=250)),
                ('slide', models.CharField(max_length=25)),
                ('posizione', models.CharField(max_length=25)),
                ('lingua', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.lingua')),
            ],
            options={
                'verbose_name': 'testo',
                'verbose_name_plural': 'testi',
                'db_table': 'testo',
            },
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=25)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.candidato')),
            ],
            options={
                'verbose_name': 'titolo',
                'verbose_name_plural': 'titoli',
                'db_table': 'titolo',
            },
        ),
        migrations.CreateModel(
            name='Linguaconosciuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lingua', models.CharField(max_length=25)),
                ('livello', models.CharField(max_length=25)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.candidato')),
            ],
            options={
                'verbose_name': 'lingua_conosciuta',
                'verbose_name_plural': 'lingue_conosciuta',
                'db_table': 'lingua_conosciuta',
            },
        ),
        migrations.CreateModel(
            name='Esperienza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professione', models.CharField(max_length=25)),
                ('durata', models.IntegerField()),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.candidato')),
            ],
            options={
                'verbose_name': 'esperienza',
                'verbose_name_plural': 'esperienze',
                'db_table': 'eseperienza',
            },
        ),
        migrations.CreateModel(
            name='CandidatoParametro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.candidato')),
                ('parametro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.aziendalingua')),
            ],
            options={
                'verbose_name': 'candidato_parametro',
                'verbose_name_plural': 'candidato_parametri',
                'db_table': 'candidato_parametro',
            },
        ),
        migrations.CreateModel(
            name='CandidatoAzienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giorno', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('azienda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.aziendalingua')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.candidato')),
            ],
            options={
                'verbose_name': 'candidato_azienda',
                'verbose_name_plural': 'candidato_aziende',
                'db_table': 'candidato_azienda',
            },
        ),
        migrations.AddField(
            model_name='aziendalingua',
            name='lingua',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.lingua'),
        ),
        migrations.CreateModel(
            name='Anagrafica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('cognome', models.CharField(max_length=25)),
                ('codicefiscale', models.CharField(max_length=10)),
                ('eta', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('stato', models.CharField(max_length=20)),
                ('provincia', models.CharField(max_length=20)),
                ('comune', models.CharField(max_length=20)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.candidato')),
            ],
            options={
                'verbose_name': 'anagrafica',
                'verbose_name_plural': 'anagrafiche',
                'db_table': 'anagrafica',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Risposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valutazione', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=1)),
                ('domanda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.questionariodomanda')),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.candidato')),
            ],
            options={
                'verbose_name': 'risposta',
                'verbose_name_plural': 'risposte',
                'db_table': 'risposta',
                'unique_together': {('utente', 'domanda')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='aziendalingua',
            unique_together={('azienda', 'lingua')},
        ),
    ]