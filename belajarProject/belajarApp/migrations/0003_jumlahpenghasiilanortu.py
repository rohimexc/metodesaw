# Generated by Django 4.1 on 2022-09-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belajarApp', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='JumlahPenghasiilanOrtu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penghasilanortu', models.CharField(max_length=100)),
                ('bobot', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
