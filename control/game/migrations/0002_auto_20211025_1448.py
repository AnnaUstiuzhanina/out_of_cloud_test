# Generated by Django 3.2.8 on 2021-10-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='gameuser',
            name='email',
            field=models.EmailField(max_length=255, primary_key=True, serialize=False, verbose_name='Почта'),
        ),
    ]
