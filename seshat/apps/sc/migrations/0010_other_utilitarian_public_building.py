# Generated by Django 4.0.3 on 2024-01-15 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_seshat_task_task_url'),
        ('core', '0056_religion'),
        ('sc', '0009_alter_fastest_individual_communication_fastest_individual_communication_from_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other_utilitarian_public_building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Evidenced'), ('SSP', 'Suspected'), ('IFR', 'Inferred')], default='TRS', max_length=5)),
                ('is_disputed', models.BooleanField(blank=True, default=False, null=True)),
                ('is_uncertain', models.BooleanField(blank=True, default=False, null=True)),
                ('expert_reviewed', models.BooleanField(blank=True, default=True, null=True)),
                ('drb_reviewed', models.BooleanField(blank=True, default=False, null=True)),
                ('name', models.CharField(default='Other_utilitarian_public_building', max_length=100)),
                ('other_utilitarian_public_building', models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500)),
                ('citations', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.seshatcomment')),
                ('curator', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='accounts.seshat_expert')),
                ('polity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity')),
            ],
            options={
                'verbose_name': 'Other_utilitarian_public_building',
                'verbose_name_plural': 'Other_utilitarian_public_buildings',
                'ordering': ['year_from', 'year_to'],
            },
        ),
    ]
