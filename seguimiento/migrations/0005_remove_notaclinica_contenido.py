from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0004_move_contenido_to_observaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notaclinica',
            name='contenido',
        ),
    ]
