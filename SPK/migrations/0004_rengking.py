# Generated by Django 4.1.5 on 2023-05-12 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SPK', '0003_alter_kriteria_bobot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rengking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rumah', models.CharField(max_length=50)),
                ('penghasilan', models.CharField(max_length=50)),
                ('bumil_bunsui', models.CharField(max_length=50)),
                ('lansia', models.CharField(max_length=50)),
                ('anak_sekolah', models.CharField(max_length=50)),
                ('total_nilai', models.FloatField()),
                ('ket', models.CharField(max_length=50)),
                ('alternatif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SPK.alternatif')),
            ],
        ),
    ]