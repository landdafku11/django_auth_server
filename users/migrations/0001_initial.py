# Generated by Django 3.1.4 on 2021-01-21 14:22

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('common', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_agent', models.BooleanField(default=False)),
                ('is_team_lead', models.BooleanField(default=False)),
                ('is_agency_admin', models.BooleanField(default=False)),
                ('search_endpoint', models.CharField(choices=[('prod', 'prod'), ('preprod', 'preprod')], default='preprod', max_length=8)),
                ('booking_endpoint', models.CharField(choices=[('prod', 'prod'), ('preprod', 'preprod')], default='preprod', max_length=8)),
                ('password_reset_token', models.CharField(max_length=100, null=True)),
                ('password_reset_sent_at', models.DateTimeField(null=True)),
                ('agency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_agency', to='teams.agency')),
                ('common_parameters', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_common_parameters', to='common.commonparameters')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='teams.team')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]