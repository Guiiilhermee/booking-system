# Generated by Django 3.2.23 on 2024-01-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=10, null=True)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
