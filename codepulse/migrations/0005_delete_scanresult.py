# Generated by Django 5.1.1 on 2024-11-10 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codepulse', '0004_persona_alter_test_cliente_alter_test_personal'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ScanResult',
        ),
    ]