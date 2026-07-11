from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0002_medidacorporal_agua_corporal_pct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notaclinica',
            name='motivo_consulta',
            field=models.TextField(blank=True, verbose_name='Motivo de la consulta'),
        ),
        migrations.AddField(
            model_name='notaclinica',
            name='objetivos_acordados',
            field=models.TextField(blank=True, verbose_name='Objetivos acordados'),
        ),
        migrations.AddField(
            model_name='notaclinica',
            name='observaciones_clinicas',
            field=models.TextField(blank=True, verbose_name='Observaciones clínicas'),
        ),
        migrations.AddField(
            model_name='notaclinica',
            name='plan_accion',
            field=models.TextField(blank=True, verbose_name='Plan de acción / Acuerdos'),
        ),
        migrations.AddField(
            model_name='notaclinica',
            name='resumen_consulta',
            field=models.TextField(blank=True, verbose_name='Resumen de la consulta'),
        ),
        migrations.AlterField(
            model_name='notaclinica',
            name='contenido',
            field=models.TextField(blank=True, null=True, verbose_name='Contenido (Legacy)'),
        ),
    ]
