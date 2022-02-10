# Generated by Django 4.0.1 on 2022-02-07 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_song_singer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='api.singer'),
        ),
    ]
