# Generated by Django 4.0.2 on 2022-09-21 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belajarApp', '0010_rename_jumlah_anak_datasiswa_jumlah_tanggungan_orang_tua'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hasilanalisa',
            name='NISN',
            field=models.CharField(max_length=100),
        ),
    ]
