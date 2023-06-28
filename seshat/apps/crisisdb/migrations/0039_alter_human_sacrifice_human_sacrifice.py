# Generated by Django 4.0.3 on 2022-11-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0038_alter_human_sacrifice_human_sacrifice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human_sacrifice',
            name='human_sacrifice',
            field=models.CharField(choices=[('U', 'Unknown'), ('A;P', 'Scholarly disagreement'), ('P*', 'Present'), ('P', 'Inferred Present'), ('A~P', 'Transitional Period (from Absent to Present)'), ('A', 'Absent'), ('A*', 'Inferred Absent'), ('P~A', 'Transitional Period (from Present to Absent)')], max_length=500),
        ),
    ]