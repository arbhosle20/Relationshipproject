# Generated by Django 4.0 on 2022-01-04 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DepartmentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rn', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('marks', models.FloatField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DepartmentApp.dept')),
            ],
        ),
    ]
