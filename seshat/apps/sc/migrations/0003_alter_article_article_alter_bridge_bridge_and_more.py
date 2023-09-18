# Generated by Django 4.0.3 on 2023-07-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc', '0002_administrative_level_is_uncertain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='bridge',
            name='bridge',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='calendar',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='canal',
            name='canal',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='courier',
            name='courier',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='court',
            name='court',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='drinking_water_supply_system',
            name='drinking_water_supply_system',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='examination_system',
            name='examination_system',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='fiction',
            name='fiction',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='food_storage_site',
            name='food_storage_site',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='foreign_coin',
            name='foreign_coin',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='formal_legal_code',
            name='formal_legal_code',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='full_time_bureaucrat',
            name='full_time_bureaucrat',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='general_postal_service',
            name='general_postal_service',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='history',
            name='history',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='indigenous_coin',
            name='indigenous_coin',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='irrigation_system',
            name='irrigation_system',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='judge',
            name='judge',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='lists_tables_and_classification',
            name='lists_tables_and_classification',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='market',
            name='market',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='merit_promotion',
            name='merit_promotion',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='mines_or_quarry',
            name='mines_or_quarry',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='mnemonic_device',
            name='mnemonic_device',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='non_phonetic_writing',
            name='non_phonetic_writing',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='nonwritten_record',
            name='nonwritten_record',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='paper_currency',
            name='paper_currency',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='philosophy',
            name='philosophy',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='phonetic_alphabetic_writing',
            name='phonetic_alphabetic_writing',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='port',
            name='port',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='postal_station',
            name='postal_station',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='practical_literature',
            name='practical_literature',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='precious_metal',
            name='precious_metal',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='professional_lawyer',
            name='professional_lawyer',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='professional_military_officer',
            name='professional_military_officer',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='professional_priesthood',
            name='professional_priesthood',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='professional_soldier',
            name='professional_soldier',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='religious_literature',
            name='religious_literature',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='road',
            name='road',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='sacred_text',
            name='sacred_text',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='scientific_literature',
            name='scientific_literature',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='script',
            name='script',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='specialized_government_building',
            name='specialized_government_building',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
        migrations.AlterField(
            model_name='written_record',
            name='written_record',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional (Absent -> Present)'), ('P~A', 'Transitional (Present -> Absent)')], max_length=500),
        ),
    ]