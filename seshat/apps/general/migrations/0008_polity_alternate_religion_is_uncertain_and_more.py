# Generated by Django 4.0.3 on 2023-02-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_alter_polity_research_assistant_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='polity_alternate_religion',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_alternate_religion_family',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_alternate_religion_genus',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_alternative_name',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_capital',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_degree_of_centralization',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_duration',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_editor',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_expert',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_language',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_language_genus',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_linguistic_family',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_original_name',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_peak_years',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_preceding_entity',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_relationship_to_preceding_entity',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_religion',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_religion_family',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_religion_genus',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_religious_tradition',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_research_assistant',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_scale_of_supracultural_interaction',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_succeeding_entity',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_supracultural_entity',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_suprapolity_relations',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_utm_zone',
            name='is_uncertain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]