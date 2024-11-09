# Generated by Django 5.1.1 on 2024-11-05 16:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codepulse', '0002_scanresult'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('estado', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('calificacion', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codepulse.categoria')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests_como_cliente', to=settings.AUTH_USER_MODEL)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests_como_personal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('interpretacion', models.TextField(blank=True, null=True)),
                ('detalles', models.TextField(blank=True, null=True)),
                ('url_imagen_path', models.URLField(blank=True, null=True)),
                ('test', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='codepulse.test')),
            ],
        ),
    ]
