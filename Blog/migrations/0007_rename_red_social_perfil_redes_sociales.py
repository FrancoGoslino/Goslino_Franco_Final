# Generated by Django 4.1.7 on 2023-03-31 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_rename_redes_sociales_perfil_red_social'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='red_social',
            new_name='redes_sociales',
        ),
    ]
