# Generated by Django 2.0.10 on 2019-01-21 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nzoz', '0002_day_specialty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nzoz.Clinic')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nzoz.Specialty')),
            ],
        ),
    ]
