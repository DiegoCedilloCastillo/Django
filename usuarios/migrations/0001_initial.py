# Generated by Django 5.1.3 on 2024-11-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('clave', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Django',
            },
        ),
    ]
