# Generated by Django 3.2.7 on 2021-09-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabel',
            name='public',
            field=models.CharField(choices=[('Keldi', 'Keldi'), ('Kelmadi', 'Kelmadi')], max_length=20),
        ),
    ]
