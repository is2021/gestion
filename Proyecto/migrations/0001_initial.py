# Generated by Django 3.1.7 on 2021-05-04 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('objetivo', models.CharField(max_length=300)),
                ('fecha_ini', models.DateField()),
                ('fecha_limite', models.DateField()),
                ('cant_dias_atrasados', models.IntegerField(default=0)),
                ('vence_mes', models.CharField(default='NO', max_length=3)),
                ('estado', models.CharField(choices=[('ACT', 'Activo'), ('BLO', 'Bloqueado'), ('FIN', 'Finalizado')], default='ACT', max_length=15)),
                ('fase', models.CharField(choices=[('ANA', 'Analisis'), ('DIS', 'Diseño'), ('COD', 'Codificacion'), ('PRU', 'Prueba'), ('MAN', 'Mantenimiento')], default='ANA', max_length=15)),
                ('usu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]